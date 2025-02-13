####################
unpinAllChatMessages
####################

Returns: :obj:`bool`

.. automodule:: masogram.methods.unpin_all_chat_messages
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.unpin_all_chat_messages(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.unpin_all_chat_messages import UnpinAllChatMessages`
- alias: :code:`from masogram.methods import UnpinAllChatMessages`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(UnpinAllChatMessages(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return UnpinAllChatMessages(...)


As shortcut from received object
--------------------------------

- :meth:`masogram.types.chat.Chat.unpin_all_messages`
