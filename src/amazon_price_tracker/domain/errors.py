"""Errors of the domain.

@file errors.py
@brief Exceptions raised when a product cannot be read or a setting is missing.
"""


class ProductParseError(Exception):
    """A product could not be read from the page."""


class PriceNotFoundError(ProductParseError):
    """The page has no readable price."""


class TitleNotFoundError(ProductParseError):
    """The page has no product title."""


class RobotCheckError(ProductParseError):
    """The page is a robot check, not a product page."""


class MissingSettingError(Exception):
    """A required setting is missing or empty."""


class InvalidSettingError(Exception):
    """A setting has a value that is not allowed."""
