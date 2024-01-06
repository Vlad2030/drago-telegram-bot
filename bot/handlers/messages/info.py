from aiogram import Router, types
from aiogram.filters import Command

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

             f"Price: <code>{token_info.priceUsd}$ ({token_info.priceNative} SOL)</code>\n\n"

             f"Liquidity: <code>{beatifier(token_info.liquidity.usd)}$</code>\n"
             f"FDV: <code>{beatifier(token_info.fdv)}$</code>\n"
             f"Market Cap: <code>{beatifier(token_info.fdv)}$</code>\n\n"

             f"Price changes:\n"
             f"5m: <code>{token_info.priceChange.m5}%</code>\n"
             f"1h: <code>{token_info.priceChange.h1}%</code>\n"
             f"6h: <code>{token_info.priceChange.h6}%</code>\n"
             f"24h: <code>{token_info.priceChange.h24}%</code>\n\n"

             f"Volumes:\n"
             f"5m: <code>{beatifier(token_info.volume.m5)}$</code>\n"
             f"1h: <code>{beatifier(token_info.volume.h1)}$</code>\n"
             f"6h: <code>{beatifier(token_info.volume.h6)}$</code>\n"
             f"24h: <code>{beatifier(token_info.volume.h24)}$</code>\n\n"

             f"CA: <code>{token_info.baseToken.address}</code>\n\n"

             f"{token_info.url}",
        disable_web_page_preview=True,
    )
