from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from core.crud.exchanges import ExchangesInfoCRUD
from core.crud.total import TotalInfoCRUD
from keyboards.inline import InlineKeyboards
from utils import log_info
from utils.number_beatifier import beatifier

router = Router(name="info")


@router.message(Command("info"))
async def info_message(
        message: types.Message,
        session: AsyncSession,
        inline_keyboard=InlineKeyboards(),
) -> types.Message:
    log_info.handler(__name__, type=message)

    exchanges_info = ExchangesInfoCRUD(session)
    total_info = TotalInfoCRUD(session)

    exchanges = await exchanges_info.get_all()
    total = await total_info.get()

    await session.close()

    price_text = "\n".join([f"{exchange.name}: <code>{exchange.price}$ ({exchange.price_change}%)</code>" for exchange in exchanges])
    message_text = (
        f"{price_text}\n\n"
        
        f"24h Total Volume: <code>{beatifier(total.total_h24_volume_quote)}$ ({beatifier(total.total_h24_volume)} DRAGO)</code>\n"
        f"24h Change: <code>{beatifier(total.price_change)}%</code>\n"
        f"24h High: <code>{beatifier(total.total_h24_high)}$</code>\n"
        f"24h Low: <code>{beatifier(total.total_h24_low)}$</code>\n"
        f"All Time High: <code>{beatifier(total.total_ath)}$</code>\n"
        f"All Time Low: <code>{beatifier(total.total_atl)}$</code>"
    )

    return await message.reply(
        text=message_text,
        reply_markup=inline_keyboard.exchanges()
    )
