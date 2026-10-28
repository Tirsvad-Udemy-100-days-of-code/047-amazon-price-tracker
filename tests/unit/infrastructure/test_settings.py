import pytest

from amazon_price_tracker.constants import (
    AMAZON_URL,
    ENV_EMAIL_ADDRESS,
    ENV_EMAIL_PASSWORD,
    ENV_PRODUCT_URL,
    ENV_SMTP_ADDRESS,
    PRACTICE_URL,
)
from amazon_price_tracker.domain.errors import InvalidSettingError, MissingSettingError
from amazon_price_tracker.infrastructure.settings import (
    load_mail_settings,
    load_product_url,
)

FULL = {
    ENV_SMTP_ADDRESS: "smtp.example.test",
    ENV_EMAIL_ADDRESS: "me@example.test",
    ENV_EMAIL_PASSWORD: "s3cret-pw",
}


def test_load_mail_settings_reads_all_values() -> None:
    settings = load_mail_settings(FULL)

    assert settings.smtp_address == "smtp.example.test"
    assert settings.email_address == "me@example.test"
    assert settings.email_password == "s3cret-pw"


@pytest.mark.parametrize(
    "name", [ENV_SMTP_ADDRESS, ENV_EMAIL_ADDRESS, ENV_EMAIL_PASSWORD]
)
def test_load_mail_settings_raises_naming_missing_variable(name: str) -> None:
    environ = {key: value for key, value in FULL.items() if key != name}

    with pytest.raises(MissingSettingError, match=name):
        load_mail_settings(environ)


def test_load_mail_settings_raises_on_empty_value() -> None:
    with pytest.raises(MissingSettingError, match=ENV_EMAIL_ADDRESS):
        load_mail_settings({**FULL, ENV_EMAIL_ADDRESS: ""})


def test_load_mail_settings_names_first_missing_variable() -> None:
    with pytest.raises(MissingSettingError, match=ENV_SMTP_ADDRESS):
        load_mail_settings({})


def test_load_product_url_defaults_to_amazon() -> None:
    assert load_product_url({}) == AMAZON_URL


def test_load_product_url_defaults_when_blank() -> None:
    assert load_product_url({ENV_PRODUCT_URL: "   "}) == AMAZON_URL


def test_load_product_url_uses_override() -> None:
    assert load_product_url({ENV_PRODUCT_URL: PRACTICE_URL}) == PRACTICE_URL


def test_load_product_url_strips_whitespace() -> None:
    assert load_product_url({ENV_PRODUCT_URL: f"  {PRACTICE_URL}\n"}) == PRACTICE_URL


@pytest.mark.parametrize("value", ["http://example.test/", "ftp://x", "example.test"])
def test_load_product_url_rejects_non_https(value: str) -> None:
    with pytest.raises(InvalidSettingError, match=ENV_PRODUCT_URL) as info:
        load_product_url({ENV_PRODUCT_URL: value})

    assert value not in str(info.value)


def test_mail_settings_repr_hides_password() -> None:
    assert "s3cret-pw" not in repr(load_mail_settings(FULL))


def test_missing_setting_error_does_not_contain_password() -> None:
    with pytest.raises(MissingSettingError) as info:
        load_mail_settings({**FULL, ENV_SMTP_ADDRESS: ""})

    assert "s3cret-pw" not in str(info.value)
