from aiogram import Router, types
from aiogram.filters import Command

from utils import log_info

router = Router(name="website")


@router.message(Command("website"))
async def website_message(message: types.Message) -> types.Message:
    log_info.handler(__name__, type=message)
    return await message.reply(
        text="https://drago.network"
    )