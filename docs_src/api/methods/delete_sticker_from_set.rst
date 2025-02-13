####################
deleteStickerFromSet
####################

Returns: :obj:`bool`

.. automodule:: masogram.methods.delete_sticker_from_set
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.delete_sticker_from_set(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.delete_sticker_from_set import DeleteStickerFromSet`
- alias: :code:`from masogram.methods import DeleteStickerFromSet`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(DeleteStickerFromSet(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return DeleteStickerFromSet(...)


As shortcut from received object
--------------------------------

- :meth:`masogram.types.sticker.Sticker.delete_from_set`
