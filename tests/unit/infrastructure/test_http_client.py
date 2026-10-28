import pytest
import requests

from amazon_price_tracker.constants import DEFAULT_HEADERS, REQUEST_TIMEOUT_SECONDS
from amazon_price_tracker.infrastructure.http_client import RequestsPageFetcher

Call = tuple[str, dict[str, str], float]


class FakeResponse:
    def __init__(self, text: str, status_code: int) -> None:
        self.text = text
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")


def _patch_get(monkeypatch: pytest.MonkeyPatch, response: FakeResponse) -> list[Call]:
    calls: list[Call] = []

    def fake_get(url: str, headers: dict[str, str], timeout: float) -> FakeResponse:
        calls.append((url, headers, timeout))
        return response

    monkeypatch.setattr(requests, "get", fake_get)
    return calls


def test_fetch_returns_text_using_url_and_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _patch_get(monkeypatch, FakeResponse("<p>hi</p>", 200))

    html = RequestsPageFetcher().fetch("https://example.test/")

    assert html == "<p>hi</p>"
    assert calls == [
        ("https://example.test/", dict(DEFAULT_HEADERS), REQUEST_TIMEOUT_SECONDS)
    ]


def test_fetch_sends_user_agent_and_accept_language(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _patch_get(monkeypatch, FakeResponse("", 200))

    RequestsPageFetcher().fetch("https://example.test/")

    headers = calls[0][1]
    assert headers["User-Agent"]
    assert headers["Accept-Language"]


def test_fetch_omits_host_and_trace_id_headers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _patch_get(monkeypatch, FakeResponse("", 200))

    RequestsPageFetcher().fetch("https://example.test/")

    assert "Host" not in calls[0][1]
    assert "X-Amzn-Trace-Id" not in calls[0][1]


def test_fetch_uses_overriding_headers(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _patch_get(monkeypatch, FakeResponse("", 200))

    RequestsPageFetcher(headers={"User-Agent": "custom"}).fetch("https://example.test/")

    assert calls[0][1] == {"User-Agent": "custom"}
    assert calls[0][2] == REQUEST_TIMEOUT_SECONDS


def test_default_headers_are_read_only() -> None:
    with pytest.raises(TypeError):
        DEFAULT_HEADERS["User-Agent"] = "x"  # type: ignore[index]


def test_fetch_raises_on_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_get(monkeypatch, FakeResponse("", 404))

    with pytest.raises(requests.HTTPError):
        RequestsPageFetcher().fetch("https://example.test/")
