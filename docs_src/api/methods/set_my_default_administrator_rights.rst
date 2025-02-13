###############################
setMyDefaultAdministratorRights
###############################

Returns: :obj:`bool`

.. automodule:: masogram.methods.set_my_default_administrator_rights
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.set_my_default_administrator_rights(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.set_my_default_administrator_rights import SetMyDefaultAdministratorRights`
- alias: :code:`from masogram.methods import SetMyDefaultAdministratorRights`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(SetMyDefaultAdministratorRights(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SetMyDefaultAdministratorRights(...)
