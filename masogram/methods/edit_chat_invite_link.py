from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional, Union

from ..types import ChatInviteLink
from .base import TelegramMethod


class EditChatInviteLink(TelegramMethod[ChatInviteLink]):
    """
    Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a :class:`masogram.types.chat_invite_link.ChatInviteLink` object.

    Source: https://core.telegram.org/bots/api#editchatinvitelink
    """

    __returning__ = ChatInviteLink
    __api_method__ = "editChatInviteLink"

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target channel (in the format :code:`@channelusername`)"""
    invite_link: str
    """The invite link to edit"""
    name: Optional[str] = None
    """Invite link name; 0-32 characters"""
    expire_date: Optional[Union[datetime.datetime, datetime.timedelta, int]] = None
    """Point in time (Unix timestamp) when the link will expire"""
    member_limit: Optional[int] = None
    """The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999"""
    creates_join_request: Optional[bool] = None
    """:code:`True`, if users joining the chat via the link need to be approved by chat administrators. If :code:`True`, *member_limit* can't be specified"""
