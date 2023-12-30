import asyncio

from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from core.data import BotConfig
from handlers import callbacks, messages
from loader import bot, dispatcher
from loguru import logger
from utils.logging import set_basic_logger
from utils.set_default import set_default_commands


dispatcher.include_router(router=messages.ca.router)


async def main() -> None:
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware(cache_time=60*60*24*7))
    set_basic_logger()
    await set_default_commands()
    logger.info("Bot started")
    await dispatcher.start_polling(
        bot,
        dispatcher=dispatcher,
        skip_updates=True,
    )
    logger.warning("Bot turns off")


if __name__ == "__main__":
    asyncio.run(main())
