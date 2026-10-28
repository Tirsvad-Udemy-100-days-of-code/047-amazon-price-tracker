"""Composition root.

@file main.py
@brief Builds the adapters, prints the product and sends a price alert.
"""

import os
import sys

from dotenv import find_dotenv, load_dotenv

from amazon_price_tracker.application.alert import check_price
from amazon_price_tracker.constants import TARGET_PRICE
from amazon_price_tracker.domain.errors import (
    InvalidSettingError,
    MissingSettingError,
    ProductParseError,
    RobotCheckError,
)
from amazon_price_tracker.infrastructure.http_client import RequestsPageFetcher
from amazon_price_tracker.infrastructure.mailer import SmtpNotifier
from amazon_price_tracker.infrastructure.scraper import SoupProductParser
from amazon_price_tracker.infrastructure.settings import (
    load_mail_settings,
    load_product_url,
)


def main() -> None:
    """Print the product and send an e-mail when its price is below target."""
    load_dotenv(find_dotenv(usecwd=True))
    try:
        settings = load_mail_settings(os.environ)
        url = load_product_url(os.environ)
    except (MissingSettingError, InvalidSettingError) as error:
        print(f"{error}. Copy .env.example to .env and fill it in.", file=sys.stderr)
        return
    notifier = SmtpNotifier(settings)
    try:
        result = check_price(
            RequestsPageFetcher(), SoupProductParser(), notifier, url, TARGET_PRICE
        )
    except RobotCheckError:
        print(
            "Amazon returned a robot check page, so there is no price to read. "
            "Try again later or set PRODUCT_URL to another page. "
            "The bot does not try to get past the check.",
            file=sys.stderr,
        )
        return
    except ProductParseError as error:
        print(f"Could not read the product: {error}", file=sys.stderr)
        return
    print(result.product.title)
    print(result.product.price)
    print("Alert sent" if result.alert_sent else "Price is not below the target")
