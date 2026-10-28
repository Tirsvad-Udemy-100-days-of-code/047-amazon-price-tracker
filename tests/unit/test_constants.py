"""Smoke tests for the constants module.

@file test_constants.py
@brief Checks the shape of the constants.
"""

from amazon_price_tracker import constants

ENV_NAMES: list[str] = [
    constants.ENV_SMTP_ADDRESS,
    constants.ENV_EMAIL_ADDRESS,
    constants.ENV_EMAIL_PASSWORD,
    constants.ENV_PRODUCT_URL,
]


def test_urls_use_https() -> None:
    """Both product URLs are https."""
    assert constants.PRACTICE_URL.startswith("https://")
    assert constants.AMAZON_URL.startswith("https://")


def test_target_price_is_positive_float() -> None:
    """The target price is a positive float."""
    assert isinstance(constants.TARGET_PRICE, float)
    assert constants.TARGET_PRICE > 0


def test_env_names_are_non_empty() -> None:
    """Every environment variable name has text."""
    assert all(name.strip() for name in ENV_NAMES)


def test_env_names_are_unique() -> None:
    """No two environment variable names collide."""
    assert len(set(ENV_NAMES)) == len(ENV_NAMES)


def test_smtp_port_is_starttls_port() -> None:
    """The SMTP port is 587."""
    assert constants.SMTP_PORT == 587
