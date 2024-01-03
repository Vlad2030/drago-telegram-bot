from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.markdown import hcode

from core.data.config import BotConfig
from core.dex_screnner import DexScrenner
from utils import log_info
from utils.number_beatifier import beatifier

router = Router(name="info")


@router.message(Command("info"))
async def info_message(message: types.Message) -> types.Message:
    log_info.handler(__name__, type=message)
    dex_screnner = DexScrenner()
    token_info = (await dex_screnner.tokens(
        ca=BotConfig.DRAGO_CONTRACT_ADDRESS,
    )).pairs[0]
    return await message.reply(
        text=f"🐲 ${token_info.baseToken.symbol}\n\n"

             f"Price: {hcode(token_info.priceUsd, '$')} "
             f"({hcode(token_info.priceNative, 'SOL')})\n\n"

             f"Liquidity: {hcode(beatifier(token_info.liquidity.usd), '$')}\n"
             f"FDV: {hcode(beatifier(token_info.fdv), '$')}\n"
             f"Market Cap: {hcode(beatifier(token_info.fdv), '$')}\n\n"

             f"Price changes:\n"
             f"5m: {hcode(token_info.priceChange.m5, '%')}\n"
             f"1h: {hcode(token_info.priceChange.h1, '%')}\n"
             f"6h: {hcode(token_info.priceChange.h6, '%')}\n"
             f"24h: {hcode(token_info.priceChange.h24, '%')}\n\n"

             f"Volumes:\n"
             f"5m: {hcode(beatifier(token_info.volume.m5), '$')}\n"
             f"1h: {hcode(beatifier(token_info.volume.h1), '$')}\n"
             f"6h: {hcode(beatifier(token_info.volume.h6), '$')}\n"
             f"24h: {hcode(beatifier(token_info.volume.h24), '$')}\n\n"

             f"CA: {hcode(token_info.baseToken.address)}\n\n"

             f"{token_info.url}",
        disable_web_page_preview=True,
    )