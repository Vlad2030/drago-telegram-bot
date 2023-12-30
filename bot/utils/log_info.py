import typing

from aiogram import types
from loguru import logger


def handler(
        func,
        type: typing.Union[types.Message, types.CallbackQuery],
) -> None:
    """log info from user message/callback

    args:
        func: function name (__name__)
        **type: Message | CallbackQuery: user message/callback

    returns:
        something like this
        `datetime | INFO     | utils.log_info:message:6 - function_name from fullname (@username) id: user_id`
    """
    return logger.info(
        "{mes} from {fullname} (@{username}) id: {id}",
        mes=func,
        id=type.from_user.id,
        username=type.from_user.username,
        fullname=type.from_user.full_name,
    )

def state(
        func,
        type: typing.Union[types.Message, types.CallbackQuery],
) -> None:
    """log info from state

    args:
        func: function name (__name__)
        state (context.FSMContext): state
        **type: Message | CallbackQuery: user message/callback

    returns:
        something like this
        `datetime | INFO     | utils.log_info:message:6 - function_name state_text state data from fullname (@username) id: user_id`
    """
    return logger.info(
        "{mes} state data from {fullname} (@{username}) id: {id}",
        mes=func,
        id=type.from_user.id,
        username=type.from_user.username,
        fullname=type.from_user.full_name,
    )

def new_admin(
        func,
        admin_data: dict,
) -> None:
    return logger.info(
        "{mes} added new admin {fullname} (@{username}) id: {id}",
        mes=func,
        id=admin_data["user_id"],
        username=admin_data["username"],
        fullname=admin_data["full_name"],
    )

def remove_admin(
        func,
        admin_username: str,
        admin_id: int,
) -> None:
    return logger.info(
        "{mes} @{user} removed admin via ID {id}",
        mes=func,
        user=admin_username,
        id=admin_id["user_id"],
    )

def new_user(
        func,
        user_data: dict,
) -> None:
    return logger.info(
        "{mes} added new user {fullname} (@{username}) number: {number}",
        mes=func,
        fullname=user_data["full_name"],
        username=user_data["username"],
        number=user_data["phone_number"],
    )