import pytest
import requests

from amazon_price_tracker.constants import REQUEST_TIMEOUT_SECONDS
from amazon_price_tracker.infrastructure.http_client import RequestsPageFetcher


class FakeResponse:
    def __init__(self, text: str, status_code: int) -> None:
        self.text = text
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")


def _patch_get(
    monkeypatch: pytest.MonkeyPatch, response: FakeResponse
) -> list[tuple[str, float]]:
    calls: list[tuple[str, float]] = []

    def fake_get(url: str, timeout: float) -> FakeResponse:
        calls.append((url, timeout))
        return response

    monkeypatch.setattr(requests, "get", fake_get)
    return calls


def test_fetch_returns_text_using_url_and_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _patch_get(monkeypatch, FakeResponse("<p>hi</p>", 200))

    html = RequestsPageFetcher().fetch("https://example.test/")

    assert html == "<p>hi</p>"
    assert calls == [("https://example.test/", REQUEST_TIMEOUT_SECONDS)]


def test_fetch_raises_on_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_get(monkeypatch, FakeResponse("", 404))

    with pytest.raises(requests.HTTPError):
        RequestsPageFetcher().fetch("https://example.test/")
