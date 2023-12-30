import typing

from aiogram import types


class Commands(types.BotCommand):
    def __init__(self: typing.Any) -> None:
        pass

    def start(self) -> types.BotCommand:
        return types.BotCommand(
            command="start",
            description="Начать пользоваться ботом",
        )

    def help(self) -> types.BotCommand:
        return types.BotCommand(
            command="help",
            description="Показать команды бота",
        )

    def menu(self) -> types.BotCommand:
        return types.BotCommand(
            command="menu",
            description="Меню бота",
        )

    def sniper(self) -> types.BotCommand:
        return types.BotCommand(
            command="sniper",
            description="Включить снайпера",
        )

    def status(self) -> types.BotCommand:
        return types.BotCommand(
            command="status",
            description="Поменять статус работы",
        )

    def profile_stats(self) -> types.BotCommand:
        return types.BotCommand(
            command="profile_stats",
            description="Статистика профиля",
        )

    def order_stats(self) -> types.BotCommand:
        return types.BotCommand(
            command="order_stats",
            description="Статистика заказов",
        )

    def about(self) -> types.BotCommand:
        return types.BotCommand(
            command="about",
            description="Информация об аккаунте",
        )
