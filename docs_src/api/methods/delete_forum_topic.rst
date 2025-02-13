################
deleteForumTopic
################

Returns: :obj:`bool`

.. automodule:: masogram.methods.delete_forum_topic
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.delete_forum_topic(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.delete_forum_topic import DeleteForumTopic`
- alias: :code:`from masogram.methods import DeleteForumTopic`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(DeleteForumTopic(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return DeleteForumTopic(...)
