from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.markdown import hcode
from utils import log_info, request
from core.data.config import BotConfig

router = Router(name="ca")


@router.message(Command("ca"))
async def ca_message(message: types.Message) -> types.Message:
    log_info.handler(__name__, type=message)
    return await message.answer(
        text=f"$DRAGO contract address - {hcode(BotConfig.DRAGO_CONTRACT_ADDRESS)} "
             "(click to copy)"
    )
