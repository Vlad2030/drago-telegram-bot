from aiogram import Router, types

from core.data.config import BotConfig
from keyboards.inline import InlineKeyboards

router = Router(name="new_post")


@router.channel_post()
async def info_message(
        channel_post: types.Message,
        inline_keyboard = InlineKeyboards(),
) -> types.Message:
    chat_lang = None
    if channel_post.sender_chat.id == int(BotConfig.DRAGO_TELEGRAM_CHANNEL_ID_RU):
        chat_lang = "RU"
    elif channel_post.sender_chat.id == int(BotConfig.DRAGO_TELEGRAM_CHANNEL_ID_EN):
        chat_lang = "EN"

    if chat_lang is not None:
        welcome_message_text = (
            "🐲🐲🐲 Дракончики,\n"
            "в этом сообщении собраны все необходимые ссылки и "
            "гайды к покупке связанным с проектом $Drago.\n\n"
            if chat_lang == "RU" else
            "🐲🐲🐲 Dragons,\n"
            "this message contains all the necessary links and "
            "guides to purchase related to the $Drago project.\n\n"
        )
        return await channel_post.reply(
            text=f"{welcome_message_text}"
                f"CA: <code>{BotConfig.DRAGO_CONTRACT_ADDRESS}</code>",
            reply_markup=inline_keyboard.new_post_keyboard(chat_lang),
        )
