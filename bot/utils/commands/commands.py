import typing

from aiogram import types


class Commands(types.BotCommand):
    def __init__(self: typing.Any) -> None:
        pass

    def ca(self) -> types.BotCommand:
        return types.BotCommand(
            command="ca",
            description="Contract address",
        )

    def info(self) -> types.BotCommand:
        return types.BotCommand(
            command="info",
            description="Info",
        )

    def price(self) -> types.BotCommand:
        return types.BotCommand(
            command="price",
            description="Price",
        )
