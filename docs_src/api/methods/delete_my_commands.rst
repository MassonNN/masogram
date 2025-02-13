################
deleteMyCommands
################

Returns: :obj:`bool`

.. automodule:: masogram.methods.delete_my_commands
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.delete_my_commands(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.delete_my_commands import DeleteMyCommands`
- alias: :code:`from masogram.methods import DeleteMyCommands`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(DeleteMyCommands(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return DeleteMyCommands(...)
