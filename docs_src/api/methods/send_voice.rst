#########
sendVoice
#########

Returns: :obj:`Message`

.. automodule:: masogram.methods.send_voice
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: Message = await bot.send_voice(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.send_voice import SendVoice`
- alias: :code:`from masogram.methods import SendVoice`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: Message = await bot(SendVoice(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SendVoice(...)


As shortcut from received object
--------------------------------

- :meth:`masogram.types.message.Message.answer_voice`
- :meth:`masogram.types.message.Message.reply_voice`
