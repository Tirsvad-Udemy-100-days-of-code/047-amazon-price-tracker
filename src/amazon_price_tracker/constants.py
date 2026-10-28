"""Constants of the Amazon price tracker.

@file constants.py
@brief The only place that defines constants (URLs, limits, environment names).
"""

from typing import Final

## @brief Practice page used instead of Amazon while developing.
PRACTICE_URL: Final[str] = "https://appbrewery.github.io/instant_pot/"

## @brief Amazon product page to track.
AMAZON_URL: Final[str] = (
    "https://www.amazon.com/dp/B075CYMYK6"
    "?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
)

## @brief Price below which an alert is sent.
# The assignment asks for a floating point price, so float is used here
# although money is normally Decimal.
TARGET_PRICE: Final[float] = 100.0

## @brief Seconds to wait for an HTTP response.
REQUEST_TIMEOUT_SECONDS: Final[int] = 10

## @brief SMTP submission port (STARTTLS).
SMTP_PORT: Final[int] = 587

## @brief Environment variable holding the SMTP server address.
ENV_SMTP_ADDRESS: Final[str] = "SMTP_ADDRESS"

## @brief Environment variable holding the sender e-mail address.
ENV_EMAIL_ADDRESS: Final[str] = "EMAIL_ADDRESS"

## @brief Environment variable holding the e-mail password.
ENV_EMAIL_PASSWORD: Final[str] = "EMAIL_PASSWORD"

## @brief Environment variable that optionally overrides the product URL.
ENV_PRODUCT_URL: Final[str] = "PRODUCT_URL"
