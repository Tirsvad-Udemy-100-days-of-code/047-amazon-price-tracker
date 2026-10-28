"""Use case: alert when the price is below the target.

@file alert.py
@brief Builds the alert message and sends it when the price is low enough.
"""

from dataclasses import dataclass

from amazon_price_tracker.application.ports import (
    Notifier,
    PageFetcher,
    ProductParser,
)
from amazon_price_tracker.application.read_product import read_product
from amazon_price_tracker.domain.alert_message import AlertMessage
from amazon_price_tracker.domain.pricing import is_below_target
from amazon_price_tracker.domain.product import Product

## @brief Subject of every price alert.
ALERT_SUBJECT = "Amazon Price Alert!"


@dataclass(frozen=True, slots=True)
class PriceCheck:
    """Result of a price check."""

    ## @brief The product read from the page.
    product: Product
    ## @brief True when an alert was sent.
    alert_sent: bool


def build_message(title: str, price: float, url: str) -> AlertMessage:
    """Return the alert for a product.

    @param title Product title.
    @param price Current price.
    @param url Link to buy the product.
    @return The message with title, price and link in the body.
    """
    return AlertMessage(
        subject=ALERT_SUBJECT,
        body=f"{title} is now ${price:.2f}\n{url}",
    )


def check_price(
    fetcher: PageFetcher,
    parser: ProductParser,
    notifier: Notifier,
    url: str,
    target: float,
) -> PriceCheck:
    """Send an alert when the product at url costs less than target.

    @param fetcher Port that downloads the page.
    @param parser Port that reads the product from the HTML.
    @param notifier Port that sends the alert.
    @param url Address of the product page.
    @param target Price under which an alert is sent.
    @return The product read and whether an alert was sent.
    @throws ProductParseError When the page holds no readable product.
    """
    product = read_product(fetcher, parser, url)
    if not is_below_target(product.price, target):
        return PriceCheck(product, alert_sent=False)
    notifier.send(build_message(product.title, product.price, url))
    return PriceCheck(product, alert_sent=True)
