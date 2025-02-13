#################
setChatMenuButton
#################

Returns: :obj:`bool`

.. automodule:: masogram.methods.set_chat_menu_button
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.set_chat_menu_button(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.set_chat_menu_button import SetChatMenuButton`
- alias: :code:`from masogram.methods import SetChatMenuButton`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(SetChatMenuButton(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SetChatMenuButton(...)
