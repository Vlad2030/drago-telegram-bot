from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from core.crud.exchanges import ExchangesInfoCRUD
from core.data.config import BotConfig
from keyboards.inline import InlineKeyboards
from utils import log_info

router = Router(name="price")


@router.message(Command("price"))
async def price_message(
        message: types.Message,
        session: AsyncSession,
        inline_keyboard=InlineKeyboards(),
) -> types.Message:
    log_info.handler(__name__, type=message)

    chat_lang = "EN"

    if message.chat.id == int(BotConfig.DRAGO_TELEGRAM_CHAT_ID_RU):
        chat_lang = "RU"

    exchanges_info = ExchangesInfoCRUD(session)
    exchanges = await exchanges_info.get_all()

    price_text = "\n".join([f"{exchange.name}: <code>{exchange.price}$ ({'+' if exchange.price_change >= 0 else ''}{exchange.price_change:.2f}%)</code>" for exchange in exchanges])

    return await message.reply(
        text=f"🐲 $DRAGO\n\n"
             f"{price_text}",
        reply_markup=inline_keyboard.ad(chat_lang)
    )