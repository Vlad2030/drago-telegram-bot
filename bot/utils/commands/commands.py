import typing

from aiogram import types


class Commands(types.BotCommand):
    def __init__(self: typing.Any) -> None:
        pass

    def ca(self) -> types.BotCommand:
        return types.BotCommand(
            command="ca",
            description="$DRAGO contract address",
        )

    def info(self) -> types.BotCommand:
        return types.BotCommand(
            command="info",
            description="$DRAGO info",
        )

    def price(self) -> types.BotCommand:
        return types.BotCommand(
            command="price",
            description="$DRAGO price",
        )

    def website(self) -> types.BotCommand:
        return types.BotCommand(
            command="website",
            description="$DRAGO website",
        )

    def links(self) -> types.BotCommand:
        return types.BotCommand(
            command="links",
            description="$DRAGO links",
        )
