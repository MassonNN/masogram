#############
getChatMember
#############

Returns: :obj:`Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]`

.. automodule:: masogram.methods.get_chat_member
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned] = await bot.get_chat_member(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.get_chat_member import GetChatMember`
- alias: :code:`from masogram.methods import GetChatMember`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned] = await bot(GetChatMember(...))




As shortcut from received object
--------------------------------

- :meth:`masogram.types.chat.Chat.get_member`
