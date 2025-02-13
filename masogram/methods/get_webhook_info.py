from __future__ import annotations

from typing import TYPE_CHECKING

from ..types import WebhookInfo
from .base import TelegramMethod


class GetWebhookInfo(TelegramMethod[WebhookInfo]):
    """
    Use this method to get current webhook status. Requires no parameters. On success, returns a :class:`masogram.types.webhook_info.WebhookInfo` object. If the bot is using :class:`masogram.methods.get_updates.GetUpdates`, will return an object with the *url* field empty.

    Source: https://core.telegram.org/bots/api#getwebhookinfo
    """

    __returning__ = WebhookInfo
    __api_method__ = "getWebhookInfo"
