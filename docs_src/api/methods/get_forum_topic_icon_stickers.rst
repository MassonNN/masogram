#########################
getForumTopicIconStickers
#########################

Returns: :obj:`List[Sticker]`

.. automodule:: masogram.methods.get_forum_topic_icon_stickers
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: List[Sticker] = await bot.get_forum_topic_icon_stickers(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.get_forum_topic_icon_stickers import GetForumTopicIconStickers`
- alias: :code:`from masogram.methods import GetForumTopicIconStickers`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: List[Sticker] = await bot(GetForumTopicIconStickers(...))
