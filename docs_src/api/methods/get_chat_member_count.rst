##################
getChatMemberCount
##################

Returns: :obj:`int`

.. automodule:: masogram.methods.get_chat_member_count
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: int = await bot.get_chat_member_count(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.get_chat_member_count import GetChatMemberCount`
- alias: :code:`from masogram.methods import GetChatMemberCount`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: int = await bot(GetChatMemberCount(...))




As shortcut from received object
--------------------------------

- :meth:`masogram.types.chat.Chat.get_member_count`
