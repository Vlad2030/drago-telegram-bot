import asyncio

from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from core.crud.exchanges import ExchangesInfoCRUD
from core.crud.total import TotalInfoCRUD
from core.data.config import BotConfig
from keyboards.inline import InlineKeyboards
from loader import bot
from utils import log_info
from utils.number_beatifier import beatifier

router = Router(name="drago_price")


@router.message(Command("drago_price"))
async def drago_price_worker(
        message: types.Message,
        session: AsyncSession,
        inline_keyboard=InlineKeyboards(),
) -> types.Message:
    log_info.handler(__name__, type=message)

    if message.from_user.id == int(BotConfig.DEV_TELEGRAM_USER_ID):
        while True:
            exchanges_info = ExchangesInfoCRUD(session)
            total_info = TotalInfoCRUD(session)

            exchanges = await exchanges_info.get_all()
            total = await total_info.get()

            price_text = "\n".join([f"{exchange.name}: <code>{exchange.price}$ ({exchange.price_change}%)</code>" for exchange in exchanges])
            drago_price_text = (
                f"{price_text}\n\n"
                
                f"24h Total Volume: <code>{beatifier(total.total_h24_volume_quote)}$ ({beatifier(total.total_h24_volume)} DRAGO)</code>\n"
                f"24h Change: <code>{beatifier(total.price_change)}%</code>\n"
                f"24h High: <code>{beatifier(total.total_h24_high)}$</code>\n"
                f"24h Low: <code>{beatifier(total.total_h24_low)}$</code>\n"
                f"All Time High: <code>{beatifier(total.total_ath)}$</code>\n"
                f"All Time Low: <code>{beatifier(total.total_atl)}$</code>"
            )

            await bot.send_message(
                chat_id=int(BotConfig.DRAGO_PRICE_TELEGRAM_CHANNEL_ID),
                text=drago_price_text,
                reply_markup=inline_keyboard.exchanges(exchanges),
            )

            asyncio.sleep(60.00)
