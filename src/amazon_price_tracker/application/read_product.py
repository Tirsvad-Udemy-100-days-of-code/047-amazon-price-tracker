"""Use case: read a product from a page.

@file read_product.py
@brief Fetches a page and parses the product on it.
"""

from amazon_price_tracker.application.ports import PageFetcher, ProductParser
from amazon_price_tracker.domain.product import Product


def read_product(fetcher: PageFetcher, parser: ProductParser, url: str) -> Product:
    """Fetch the page at url and return its product.

    @param fetcher Port that downloads the page.
    @param parser Port that reads the product from the HTML.
    @param url Address of the product page.
    @return The product on the page.
    @throws ProductParseError When the page holds no readable product.
    """
    return parser.parse(fetcher.fetch(url))
