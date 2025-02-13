from inspect import isclass
from typing import Any, Dict, Optional, Sequence, Type, Union, cast

from masogram.filters.base import Filter
from masogram.fsm.state import State, StatesGroup
from masogram.types import TelegramObject

StateType = Union[str, None, State, StatesGroup, Type[StatesGroup]]


class StateFilter(Filter):
    """
    State filter
    """

    __slots__ = ("states",)

    def __init__(self, *states: StateType) -> None:
        if not states:
            raise ValueError("At least one state is required")

        self.states = states

    def __str__(self) -> str:
        return self._signature_to_string(
            *self.states,
        )

    async def __call__(
        self, obj: Union[TelegramObject], raw_state: Optional[str] = None
    ) -> Union[bool, Dict[str, Any]]:
        allowed_states = cast(Sequence[StateType], self.states)
        for allowed_state in allowed_states:
            if isinstance(allowed_state, str) or allowed_state is None:
                if allowed_state == "*" or raw_state == allowed_state:
                    return True
            elif isinstance(allowed_state, (State, StatesGroup)):
                if allowed_state(event=obj, raw_state=raw_state):
                    return True
            elif isclass(allowed_state) and issubclass(allowed_state, StatesGroup):
                if allowed_state()(event=obj, raw_state=raw_state):
                    return True
        return False
