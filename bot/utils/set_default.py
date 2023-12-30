from aiogram.methods import SetMyCommands

from loader import bot
from utils.commands import Commands


async def set_default_commands() -> None:
    commands = Commands()
    return await bot(
        SetMyCommands(
            commands=[
                commands.ca(),
            ],
        ),
    )
