"""SMTP adapter for the Notifier port.

@file mailer.py
@brief Sends the alert to your own address with smtplib and STARTTLS.
"""

import smtplib
from collections.abc import Callable
from email.message import EmailMessage

from amazon_price_tracker.constants import SMTP_PORT
from amazon_price_tracker.domain.alert_message import AlertMessage
from amazon_price_tracker.infrastructure.settings import MailSettings


class SmtpNotifier:
    """Notifier port implemented with smtplib."""

    def __init__(
        self,
        settings: MailSettings,
        smtp_factory: Callable[..., smtplib.SMTP] = smtplib.SMTP,
    ) -> None:
        """Keep the settings and the SMTP connection factory.

        @param settings Server, address and password.
        @param smtp_factory Creates the connection; replaced in tests.
        """
        self._settings = settings
        self._smtp_factory = smtp_factory

    def _build(self, message: AlertMessage) -> bytes:
        email = EmailMessage()
        email["Subject"] = message.subject
        email["From"] = self._settings.email_address
        email["To"] = self._settings.email_address
        email.set_content(message.body, charset="utf-8")
        return email.as_bytes()

    def send(self, message: AlertMessage) -> None:
        """Send message from the sender address to the same address.

        @param message Subject and body to send.
        @throws smtplib.SMTPException When the server refuses the login or message.
        """
        settings = self._settings
        with self._smtp_factory(settings.smtp_address, port=SMTP_PORT) as connection:
            connection.starttls()
            connection.login(settings.email_address, settings.email_password)
            connection.sendmail(
                from_addr=settings.email_address,
                to_addrs=settings.email_address,
                msg=self._build(message),
            )
