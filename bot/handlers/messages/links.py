from aiogram import Router, types
from aiogram.filters import Command

from core.data.config import BotConfig
from keyboards.inline import InlineKeyboards

router = Router(name="links")


@router.message(Command("links"))
async def info_message(
        message: types.Message,
        inline_keyboard = InlineKeyboards(),
) -> types.Message:
    chat_lang = None
    if message.sender_chat.id == int(BotConfig.DRAGO_TELEGRAM_CHANNEL_ID_RU):
        chat_lang = "RU"
    elif message.sender_chat.id == int(BotConfig.DRAGO_TELEGRAM_CHANNEL_ID_EN):
        chat_lang = "EN"

    if chat_lang is not None:
        welcome_message_text = (
            "В этом сообщении собраны все необходимые ссылки и "
            "гайды к покупке связанным с проектом $Drago.\n\n"
            if chat_lang == "RU" else
            "This message contains all the necessary links and "
            "guides to purchase related to the $Drago project.\n\n"
        )
        return await message.reply(
            text=welcome_message_text,
            reply_markup=inline_keyboard.new_post_keyboard(chat_lang),
        )