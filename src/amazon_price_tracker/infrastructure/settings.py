"""Mail settings read from the environment.

@file settings.py
@brief Builds MailSettings from a mapping of environment variables.
"""

from collections.abc import Mapping
from dataclasses import dataclass, field

from amazon_price_tracker.constants import (
    ENV_EMAIL_ADDRESS,
    ENV_EMAIL_PASSWORD,
    ENV_SMTP_ADDRESS,
)
from amazon_price_tracker.domain.errors import MissingSettingError


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
