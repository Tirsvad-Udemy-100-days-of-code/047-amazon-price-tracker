"""Reads a product from page HTML with BeautifulSoup.

@file scraper.py
@brief Day 47 step 1: get the title and the price as a float.
"""

from bs4 import BeautifulSoup, Tag

from amazon_price_tracker.constants import (
    PRICE_SELECTORS,
    ROBOT_CHECK_MARKERS,
    TITLE_SELECTORS,
)
from amazon_price_tracker.domain.errors import (
    PriceNotFoundError,
    ProductParseError,
    RobotCheckError,
    TitleNotFoundError,
)
from amazon_price_tracker.domain.product import Product


def is_robot_check(html: str) -> bool:
    """Tell whether html is Amazon's robot-check page.

    @param html Page HTML.
    @return True when any robot-check marker is present.
    """
    return any(marker in html for marker in ROBOT_CHECK_MARKERS)


def _ensure_not_robot_check(html: str) -> None:
    if is_robot_check(html):
        raise RobotCheckError(
            "The page is a robot check, not a product page. "
            "The bot does not try to get past it."
        )


def _select_first(html: str, selectors: tuple[str, ...]) -> Tag | None:
    soup = BeautifulSoup(html, "html.parser")
    for selector in selectors:
        element = soup.select_one(selector)
        if element is not None:
            return element
    return None


def get_title(html: str) -> str:
    """Return the text of the product title element, whitespace collapsed.

    @param html Page HTML.
    @return The product title.
    @throws RobotCheckError When the page is a robot check.
    @throws TitleNotFoundError When the element is missing.
    """
    _ensure_not_robot_check(html)
    element = _select_first(html, TITLE_SELECTORS)
    if element is None:
        raise TitleNotFoundError(
            f"No element matching {', '.join(TITLE_SELECTORS)} on the page"
        )
    return " ".join(element.get_text().split())


def get_price(html: str) -> float:
    """Return the price of the first element matching a price selector.

    @param html Page HTML.
    @return The price as a floating point number.
    @throws RobotCheckError When the page is a robot check.
    @throws PriceNotFoundError When no element matches.
    @throws ProductParseError When the price text is not a number.
    """
    _ensure_not_robot_check(html)
    element = _select_first(html, PRICE_SELECTORS)
    if element is None:
        raise PriceNotFoundError(
            f"No element matching {', '.join(PRICE_SELECTORS)} on the page"
        )
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
    @throws RobotCheckError When the page is a robot check.
    @throws ProductParseError When the title or the price cannot be read.
    """
    _ensure_not_robot_check(html)
    return Product(title=get_title(html), price=get_price(html))


class SoupProductParser:
    """ProductParser port implemented with BeautifulSoup."""

    def parse(self, html: str) -> Product:
        """Return the product described by html."""
        return parse_product(html)
