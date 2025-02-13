from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..types import ShippingOption
from .base import TelegramMethod


class AnswerShippingQuery(TelegramMethod[bool]):
    """
    If you sent an invoice requesting a shipping address and the parameter *is_flexible* was specified, the Bot API will send an :class:`masogram.types.update.Update` with a *shipping_query* field to the bot. Use this method to reply to shipping queries. On success, :code:`True` is returned.

    Source: https://core.telegram.org/bots/api#answershippingquery
    """

    __returning__ = bool
    __api_method__ = "answerShippingQuery"

    shipping_query_id: str
    """Unique identifier for the query to be answered"""
    ok: bool
    """Pass :code:`True` if delivery to the specified address is possible and :code:`False` if there are any problems (for example, if delivery to the specified address is not possible)"""
    shipping_options: Optional[List[ShippingOption]] = None
    """Required if *ok* is :code:`True`. A JSON-serialized array of available shipping options."""
    error_message: Optional[str] = None
    """Required if *ok* is :code:`False`. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user."""
