from aiogram.methods import SetMyCommands
from loader import bot
from utils.commands import Commands


async def set_default_commands() -> None:
    commands = Commands()
    return await bot(
        SetMyCommands(
            commands=[
                commands.start(),
                commands.menu(),
                commands.sniper(),
                commands.status(),
                commands.profile_stats(),
                commands.order_stats(),
                commands.about(),
                commands.help(),
            ],
        ),
    )
