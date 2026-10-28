"""Errors of the domain.

@file errors.py
@brief Exceptions raised when a product cannot be read from a page.
"""


class ProductParseError(Exception):
    """A product could not be read from the page."""


class PriceNotFoundError(ProductParseError):
    """The page has no readable price."""


class TitleNotFoundError(ProductParseError):
    """The page has no product title."""
