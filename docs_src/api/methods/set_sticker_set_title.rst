##################
setStickerSetTitle
##################

Returns: :obj:`bool`

.. automodule:: masogram.methods.set_sticker_set_title
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.set_sticker_set_title(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.set_sticker_set_title import SetStickerSetTitle`
- alias: :code:`from masogram.methods import SetStickerSetTitle`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(SetStickerSetTitle(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SetStickerSetTitle(...)
