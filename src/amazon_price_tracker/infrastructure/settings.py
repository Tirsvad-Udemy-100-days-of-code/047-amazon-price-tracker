"""Mail settings read from the environment.

@file settings.py
@brief Builds MailSettings from a mapping of environment variables.
"""

from collections.abc import Mapping
from dataclasses import dataclass, field

from amazon_price_tracker.constants import (
    AMAZON_URL,
    ENV_EMAIL_ADDRESS,
    ENV_EMAIL_PASSWORD,
    ENV_PRODUCT_URL,
    ENV_SMTP_ADDRESS,
)
from amazon_price_tracker.domain.errors import InvalidSettingError, MissingSettingError


@dataclass(frozen=True, slots=True)
class MailSettings:
    """Where and how to send the alert e-mail."""

    smtp_address: str
    email_address: str
    # Kept out of repr so the secret never reaches logs or tracebacks.
    email_password: str = field(repr=False)


def _require(environ: Mapping[str, str], name: str) -> str:
    value = environ.get(name, "")
    if not value.strip():
        raise MissingSettingError(f"Missing setting: {name}")
    return value


def load_product_url(environ: Mapping[str, str]) -> str:
    """Return the product URL from environ, or the Amazon default.

    @param environ Environment variables, for example os.environ.
    @return The URL, stripped.
    @throws InvalidSettingError When the value does not start with https://.
    """
    value = environ.get(ENV_PRODUCT_URL, "").strip()
    if not value:
        return AMAZON_URL
    if not value.startswith("https://"):
        # The value is not echoed: it may be long or carry a token.
        raise InvalidSettingError(f"Invalid setting: {ENV_PRODUCT_URL} must be https")
    return value


def load_mail_settings(environ: Mapping[str, str]) -> MailSettings:
    """Return the mail settings found in environ.

    @param environ Environment variables, for example os.environ.
    @return The settings.
    @throws MissingSettingError Naming the first missing or empty variable.
    """
    return MailSettings(
        smtp_address=_require(environ, ENV_SMTP_ADDRESS),
        email_address=_require(environ, ENV_EMAIL_ADDRESS),
        email_password=_require(environ, ENV_EMAIL_PASSWORD),
    )
