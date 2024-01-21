import asyncio
import datetime


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
    message_count = 0

    if message.from_user.id == int(BotConfig.DEV_TELEGRAM_USER_ID):
        while True:
            exchanges_info = ExchangesInfoCRUD(session)
            total_info = TotalInfoCRUD(session)

            exchanges = await exchanges_info.get_all()
            total = await total_info.get()

            price_text = "\n".join([f"{exchange.name}: <code>{exchange.price}$ ({'+' if exchange.price_change > 0 else ''}{exchange.price_change:.2f}%)</code>" for exchange in exchanges])
            drago_price_text = (
                f"{price_text}\n\n"
                
                f"24h Total Volume: <code>{beatifier(total.total_h24_volume_quote)}$ ({beatifier(total.total_h24_volume)} DRAGO)</code>\n"
                f"24h Change: <code>{'+' if total.price_change > 0 else ''}{total.price_change:.2f}%</code>\n"
                f"24h High: <code>{total.total_h24_high:.4f}$</code>\n"
                f"24h Low: <code>{total.total_h24_low:.4f}$</code>\n"
                f"All Time High: <code>{total.total_ath:.4f}$</code>\n"
                f"All Time Low: <code>{total.total_atl:.4f}$</code>"
            )

            await bot.send_message(
                chat_id=int(BotConfig.DRAGO_PRICE_TELEGRAM_CHANNEL_ID),
                text=drago_price_text,
                reply_markup=inline_keyboard.exchanges(exchanges),
            )

            message_count += 1

            await message.answer(
                text=f"Success!\n\n"
                     f"Send {message_count} message, time: {datetime.datetime.now().strftime('%H:%M')}",
                disable_notification=True,
                reply_markup=inline_keyboard.ad(),
            )

            await asyncio.sleep(60.00)
