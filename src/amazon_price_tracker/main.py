"""Composition root.

@file main.py
@brief Builds the adapters, prints the product and sends a price alert.
"""

import os
import sys

from dotenv import find_dotenv, load_dotenv

from amazon_price_tracker.application.alert import check_price
from amazon_price_tracker.constants import PRACTICE_URL, TARGET_PRICE
from amazon_price_tracker.domain.errors import MissingSettingError
from amazon_price_tracker.infrastructure.http_client import RequestsPageFetcher
from amazon_price_tracker.infrastructure.mailer import SmtpNotifier
from amazon_price_tracker.infrastructure.scraper import SoupProductParser
from amazon_price_tracker.infrastructure.settings import load_mail_settings


def main() -> None:
    """Print the product and send an e-mail when its price is below target."""
    load_dotenv(find_dotenv(usecwd=True))
    try:
        settings = load_mail_settings(os.environ)
    except MissingSettingError as error:
        print(f"{error}. Copy .env.example to .env and fill it in.", file=sys.stderr)
        return
    notifier = SmtpNotifier(settings)
    result = check_price(
        RequestsPageFetcher(), SoupProductParser(), notifier, PRACTICE_URL, TARGET_PRICE
    )
    print(result.product.title)
    print(result.product.price)
    print("Alert sent" if result.alert_sent else "Price is not below the target")
