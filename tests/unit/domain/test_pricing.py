from amazon_price_tracker.domain.pricing import is_below_target


def test_is_below_target_true_when_price_lower() -> None:
    assert is_below_target(99.99, 100.0)


def test_is_below_target_false_when_price_equal() -> None:
    assert not is_below_target(100.0, 100.0)


def test_is_below_target_false_when_price_higher() -> None:
    assert not is_below_target(100.01, 100.0)
