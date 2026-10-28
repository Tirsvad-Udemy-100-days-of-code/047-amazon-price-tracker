"""Ports the use cases need from the outside.

@file ports.py
@brief Protocols for fetching a page and parsing a product from it.
"""

from typing import Protocol

from amazon_price_tracker.domain.product import Product


class PageFetcher(Protocol):
    """Fetches the HTML of a page."""

    def fetch(self, url: str) -> str:
        """Return the HTML text of the page at url."""
        ...


class ProductParser(Protocol):
    """Reads a product from HTML."""

    def parse(self, html: str) -> Product:
        """Return the product described by html."""
        ...
