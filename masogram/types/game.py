from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from .base import TelegramObject

if TYPE_CHECKING:
    from .animation import Animation
    from .message_entity import MessageEntity
    from .photo_size import PhotoSize


class Game(TelegramObject):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Source: https://core.telegram.org/bots/api#game
    """

    title: str
    """Title of the game"""
    description: str
    """Description of the game"""
    photo: List[PhotoSize]
    """Photo that will be displayed in the game message in chats."""
    text: Optional[str] = None
    """*Optional*. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls :class:`masogram.methods.set_game_score.SetGameScore`, or manually edited using :class:`masogram.methods.edit_message_text.EditMessageText`. 0-4096 characters."""
    text_entities: Optional[List[MessageEntity]] = None
    """*Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc."""
    animation: Optional[Animation] = None
    """*Optional*. Animation that will be displayed in the game message in chats. Upload via `BotFather <https://t.me/botfather>`_"""
