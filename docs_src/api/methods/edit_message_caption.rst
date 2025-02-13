##################
editMessageCaption
##################

Returns: :obj:`Union[Message, bool]`

.. automodule:: masogram.methods.edit_message_caption
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: Union[Message, bool] = await bot.edit_message_caption(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.edit_message_caption import EditMessageCaption`
- alias: :code:`from masogram.methods import EditMessageCaption`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: Union[Message, bool] = await bot(EditMessageCaption(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return EditMessageCaption(...)


As shortcut from received object
--------------------------------

- :meth:`masogram.types.message.Message.edit_caption`
