from email import message_from_bytes, policy
from types import TracebackType
from typing import Any, cast

from amazon_price_tracker.constants import SMTP_PORT
from amazon_price_tracker.domain.alert_message import AlertMessage
from amazon_price_tracker.infrastructure.mailer import SmtpNotifier
from amazon_price_tracker.infrastructure.settings import MailSettings


class FakeSmtp:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.calls: list[str] = []
        self.login_args: tuple[str, str] | None = None
        self.mail: dict[str, Any] = {}
        self.closed = False

    def __enter__(self) -> "FakeSmtp":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.closed = True

    def starttls(self) -> None:
        self.calls.append("starttls")

    def login(self, user: str, password: str) -> None:
        self.calls.append("login")
        self.login_args = (user, password)

    def sendmail(self, from_addr: str, to_addrs: str, msg: bytes) -> None:
        self.calls.append("sendmail")
        self.mail = {"from": from_addr, "to": to_addrs, "msg": msg}


def _send(message: AlertMessage) -> FakeSmtp:
    created: list[FakeSmtp] = []

    def factory(host: str, port: int) -> FakeSmtp:
        created.append(FakeSmtp(host, port))
        return created[0]

    settings = MailSettings("smtp.example.test", "me@example.test", "pw")
    SmtpNotifier(settings, smtp_factory=cast(Any, factory)).send(message)
    return created[0]


def test_send_connects_to_host_on_starttls_port() -> None:
    smtp = _send(AlertMessage("Subject", "Body"))

    assert smtp.host == "smtp.example.test"
    assert smtp.port == SMTP_PORT == 587
    assert smtp.closed


def test_send_runs_starttls_login_sendmail_in_order() -> None:
    smtp = _send(AlertMessage("Subject", "Body"))

    assert smtp.calls == ["starttls", "login", "sendmail"]
    assert smtp.login_args == ("me@example.test", "pw")


def test_send_mails_to_own_address_with_utf8_content() -> None:
    body = "Pot æøå is now $9.50\nhttps://example.test/p"
    smtp = _send(AlertMessage("Amazon Price Alert!", body))

    assert smtp.mail["from"] == "me@example.test"
    assert smtp.mail["to"] == "me@example.test"
    raw = smtp.mail["msg"]
    assert isinstance(raw, bytes)
    parsed = message_from_bytes(raw, policy=policy.default)
    assert parsed["Subject"] == "Amazon Price Alert!"
    assert parsed["From"] == parsed["To"] == "me@example.test"
    content = parsed.get_content()
    assert "Pot æøå" in content
    assert "$9.50" in content
    assert "https://example.test/p" in content
    assert parsed.get_content_charset() == "utf-8"
