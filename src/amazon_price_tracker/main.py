"""Composition root.

@file main.py
@brief Builds the adapters and prints the title and price of the product.
"""

from amazon_price_tracker.application.read_product import read_product
from amazon_price_tracker.constants import PRACTICE_URL
from amazon_price_tracker.infrastructure.http_client import RequestsPageFetcher
from amazon_price_tracker.infrastructure.scraper import SoupProductParser


def main() -> None:
    """Print the title and the price of the practice product."""
    product = read_product(RequestsPageFetcher(), SoupProductParser(), PRACTICE_URL)
    print(product.title)
    print(product.price)
