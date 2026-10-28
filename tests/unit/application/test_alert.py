from amazon_price_tracker.application.alert import (
    PriceCheck,
    build_message,
    check_price,
)
from amazon_price_tracker.domain.alert_message import AlertMessage
from amazon_price_tracker.domain.product import Product

URL = "https://example.test/p"


class FakeFetcher:
    def __init__(self) -> None:
        self.urls: list[str] = []

    def fetch(self, url: str) -> str:
        self.urls.append(url)
        return "<html></html>"


class FakeParser:
    def __init__(self, product: Product) -> None:
        self.product = product

    def parse(self, html: str) -> Product:
        return self.product


class FakeNotifier:
    def __init__(self) -> None:
        self.sent: list[AlertMessage] = []

    def send(self, message: AlertMessage) -> None:
        self.sent.append(message)


def _run(price: float) -> tuple[PriceCheck, FakeNotifier, FakeFetcher]:
    notifier = FakeNotifier()
    fetcher = FakeFetcher()
    result = check_price(
        fetcher, FakeParser(Product("Pot", price)), notifier, URL, 100.0
    )
    return result, notifier, fetcher


def test_build_message_contains_title_price_and_link() -> None:
    message = build_message("Instant Pot", 79.5, URL)

    assert message.subject == "Amazon Price Alert!"
    assert "Instant Pot" in message.body
    assert "$79.50" in message.body
    assert URL in message.body


def test_check_price_sends_once_when_below_target() -> None:
    result, notifier, fetcher = _run(99.99)

    assert result.alert_sent
    assert result.product == Product("Pot", 99.99)
    assert fetcher.urls == [URL]
    assert len(notifier.sent) == 1
    assert "$99.99" in notifier.sent[0].body


def test_check_price_does_not_send_when_equal_to_target() -> None:
    result, notifier, fetcher = _run(100.0)

    assert not result.alert_sent
    assert fetcher.urls == [URL]
    assert notifier.sent == []


def test_check_price_does_not_send_when_above_target() -> None:
    result, notifier, fetcher = _run(150.0)

    assert not result.alert_sent
    assert fetcher.urls == [URL]
    assert notifier.sent == []
