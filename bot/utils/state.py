from aiogram import types
from aiogram.fsm.context import FSMContext
from schemas.user import User


class StateUpdate:
    def __init__(self, state: FSMContext) -> None:
        self.state = state

    async def user(
            self,
            message: types.Message,
            expire_as: str,
    ) -> User:
        return await self.state.update_data(
            user_id=message.forward_from.id,
            username=message.forward_from.username,
            full_name=message.forward_from.full_name,
            expire_as=expire_as,
        )
