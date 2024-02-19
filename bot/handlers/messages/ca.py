from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.markdown import hcode

from core.data.config import BotConfig
from utils import log_info

router = Router(name="ca")


@router.message(Command("ca"))
async def ca_message(message: types.Message) -> types.Message:
    log_info.handler(__name__, type=message)
    return await message.reply(
        text=f"{hcode(BotConfig.DRAGO_CONTRACT_ADDRESS)}"
    )
