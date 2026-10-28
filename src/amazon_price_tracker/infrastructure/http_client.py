"""HTTP adapter for the PageFetcher port.

@file http_client.py
@brief Downloads a page with requests.
"""

from collections.abc import Mapping

import requests

from amazon_price_tracker.constants import DEFAULT_HEADERS, REQUEST_TIMEOUT_SECONDS


class RequestsPageFetcher:
    """PageFetcher port implemented with requests."""

    def __init__(self, headers: Mapping[str, str] = DEFAULT_HEADERS) -> None:
        """Keep the headers sent with every request.

        @param headers Request headers; browser-like by default.
        """
        self._headers = headers

    def fetch(self, url: str) -> str:
        """Return the HTML text of the page at url.

        @param url Address of the page.
        @return The response body as text.
        @throws requests.HTTPError When the server answers with an error status.
        """
        response = requests.get(
            url, headers=dict(self._headers), timeout=REQUEST_TIMEOUT_SECONDS
        )
        response.raise_for_status()
        return response.text
