from aiogram import Router, types
from aiogram.filters import Command

from core.data.config import BotConfig
from core.dex_screnner import DexScrenner
from utils import log_info

router = Router(name="price")


@router.message(Command("price"))
async def price_message(message: types.Message) -> types.Message:
    log_info.handler(__name__, type=message)
    dex_screnner = DexScrenner()
    token_info = (await dex_screnner.tokens(
        ca=BotConfig.DRAGO_CONTRACT_ADDRESS,
    )).pairs[0]
    return await message.reply(
        text=f"🐲 ${token_info.baseToken.symbol}\n\n"

             f"Price: <code>{token_info.priceUsd}$ ({token_info.priceNative} SOL)</code>\n\n",
        disable_web_page_preview=True,
    )