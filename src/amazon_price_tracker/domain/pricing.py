"""Price rules.

@file pricing.py
@brief Decides whether a price is low enough to alert on.
"""


def is_below_target(price: float, target: float) -> bool:
    """Return True when price is strictly below target.

    @param price Current price.
    @param target Price under which an alert is wanted.
    @return True when price < target; an equal price is not below.
    """
    return price < target
