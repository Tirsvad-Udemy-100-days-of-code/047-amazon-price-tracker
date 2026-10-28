"""Constants of the Amazon price tracker.

@file constants.py
@brief The only place that defines constants (URLs, limits, environment names).
"""

from collections.abc import Mapping
from types import MappingProxyType
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

## @brief Browser-like request headers, read-only.
# Copied from a real browser (see httpbin.org/headers) as the lecture says,
# without Host and X-Amzn-Trace-Id. No br/zstd: requests may not decode them.
DEFAULT_HEADERS: Final[Mapping[str, str]] = MappingProxyType(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Encoding": "gzip, deflate",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
    }
)

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
