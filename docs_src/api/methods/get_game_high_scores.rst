#################
getGameHighScores
#################

Returns: :obj:`List[GameHighScore]`

.. automodule:: masogram.methods.get_game_high_scores
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: List[GameHighScore] = await bot.get_game_high_scores(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.get_game_high_scores import GetGameHighScores`
- alias: :code:`from masogram.methods import GetGameHighScores`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: List[GameHighScore] = await bot(GetGameHighScores(...))
