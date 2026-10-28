"""The alert message.

@file alert_message.py
@brief Defines the AlertMessage value object shared by use case and port.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AlertMessage:
    """A message to send to the user."""

    ## @brief Subject line.
    subject: str
    ## @brief Plain text body.
    body: str
