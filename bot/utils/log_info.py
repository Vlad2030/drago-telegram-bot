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
