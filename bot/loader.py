from aiogram import Bot, Dispatcher, enums

from core.data import BotConfig

bot = Bot(token=BotConfig.BOT_TOKEN, parse_mode=enums.ParseMode.HTML)
dispatcher = Dispatcher(bot=bot)