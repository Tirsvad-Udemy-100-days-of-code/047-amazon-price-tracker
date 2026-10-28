from pathlib import Path

import pytest

from amazon_price_tracker.domain.errors import (
    PriceNotFoundError,
    ProductParseError,
    TitleNotFoundError,
)
from amazon_price_tracker.domain.product import Product
from amazon_price_tracker.infrastructure.scraper import (
    SoupProductParser,
    get_price,
    get_title,
    parse_product,
)

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures"


def _read(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def test_get_price_returns_first_offscreen_as_float() -> None:
    price = get_price(_read("practice_page.html"))

    assert price == 99.99
    assert isinstance(price, float)


def test_get_title_returns_stripped_text() -> None:
    title = get_title(_read("practice_page.html"))

    assert title == title.strip()
    assert title.startswith("Instant Pot Duo Plus")


def test_get_price_raises_when_price_missing() -> None:
    with pytest.raises(PriceNotFoundError):
        get_price(_read("no_price_page.html"))


def test_get_title_raises_when_title_missing() -> None:
    with pytest.raises(TitleNotFoundError):
        get_title("<html></html>")


def test_get_price_raises_when_text_not_a_number() -> None:
    html = '<span class="a-offscreen">$abc</span>'

    with pytest.raises(ProductParseError):
        get_price(html)


def test_parse_product_returns_product() -> None:
    product = parse_product(_read("practice_page.html"))

    assert isinstance(product, Product)
    assert product.price == 99.99


def test_soup_product_parser_parses_html() -> None:
    product = SoupProductParser().parse(_read("practice_page.html"))

    assert product.price == 99.99
