"""The product model.

@file product.py
@brief Defines the Product value object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Product:
    """A product with its title and current price."""

    ## @brief Product title as shown on the page.
    title: str
    ## @brief Price as a float: the assignment asks for a floating point
    # number, so float is used although money is normally Decimal.
    price: float
