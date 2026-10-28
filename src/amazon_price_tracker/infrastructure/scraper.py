"""Reads a product from page HTML with BeautifulSoup.

@file scraper.py
@brief Day 47 step 1: get the title and the price as a float.
"""

from bs4 import BeautifulSoup

from amazon_price_tracker.domain.errors import (
    PriceNotFoundError,
    ProductParseError,
    TitleNotFoundError,
)
from amazon_price_tracker.domain.product import Product


def get_title(html: str) -> str:
    """Return the text of the element with id productTitle, whitespace collapsed.

    @param html Page HTML.
    @return The product title.
    @throws TitleNotFoundError When the element is missing.
    """
    element = BeautifulSoup(html, "html.parser").select_one("#productTitle")
    if element is None:
        raise TitleNotFoundError("No element with id 'productTitle' on the page")
    return " ".join(element.get_text().split())


def get_price(html: str) -> float:
    """Return the price of the first element with class a-offscreen.

    @param html Page HTML.
    @return The price as a floating point number.
    @throws PriceNotFoundError When the element is missing.
    @throws ProductParseError When the price text is not a number.
    """
    element = BeautifulSoup(html, "html.parser").select_one(".a-offscreen")
    if element is None:
        raise PriceNotFoundError("No element with class 'a-offscreen' on the page")
    text = element.get_text().strip()
    # Text looks like "$99.99": drop the currency sign, as the hint suggests.
    amount = text.split("$")[-1].replace(",", "")
    try:
        return float(amount)
    except ValueError as error:
        raise ProductParseError(f"Price text is not a number: {text!r}") from error


def parse_product(html: str) -> Product:
    """Return the product described by html.

    @param html Page HTML.
    @return The product with title and price.
    @throws ProductParseError When the title or the price cannot be read.
    """
    return Product(title=get_title(html), price=get_price(html))


class SoupProductParser:
    """ProductParser port implemented with BeautifulSoup."""

    def parse(self, html: str) -> Product:
        """Return the product described by html."""
        return parse_product(html)
