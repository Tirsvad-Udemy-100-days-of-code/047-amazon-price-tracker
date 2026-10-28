from amazon_price_tracker.application.read_product import read_product
from amazon_price_tracker.domain.product import Product


class FakeFetcher:
    def __init__(self, html: str) -> None:
        self.html = html
        self.urls: list[str] = []

    def fetch(self, url: str) -> str:
        self.urls.append(url)
        return self.html


class FakeParser:
    def __init__(self, product: Product) -> None:
        self.product = product
        self.received: list[str] = []

    def parse(self, html: str) -> Product:
        self.received.append(html)
        return self.product


def test_read_product_fetches_url_and_returns_parsed_product() -> None:
    expected = Product(title="Pot", price=9.5)
    fetcher = FakeFetcher("<html>page</html>")
    parser = FakeParser(expected)

    result = read_product(fetcher, parser, "https://example.test/p")

    assert result == expected
    assert fetcher.urls == ["https://example.test/p"]
    assert parser.received == ["<html>page</html>"]
