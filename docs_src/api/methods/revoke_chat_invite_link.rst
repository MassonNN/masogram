####################
revokeChatInviteLink
####################

Returns: :obj:`ChatInviteLink`

.. automodule:: masogram.methods.revoke_chat_invite_link
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: ChatInviteLink = await bot.revoke_chat_invite_link(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.revoke_chat_invite_link import RevokeChatInviteLink`
- alias: :code:`from masogram.methods import RevokeChatInviteLink`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: ChatInviteLink = await bot(RevokeChatInviteLink(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return RevokeChatInviteLink(...)


As shortcut from received object
--------------------------------

- :meth:`masogram.types.chat.Chat.revoke_invite_link`
