"""HTTP adapter for the PageFetcher port.

@file http_client.py
@brief Downloads a page with requests.
"""

import requests

from amazon_price_tracker.constants import REQUEST_TIMEOUT_SECONDS


class RequestsPageFetcher:
    """PageFetcher port implemented with requests."""

    def fetch(self, url: str) -> str:
        """Return the HTML text of the page at url.

        @param url Address of the page.
        @return The response body as text.
        @throws requests.HTTPError When the server answers with an error status.
        """
        response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
        response.raise_for_status()
        return response.text
