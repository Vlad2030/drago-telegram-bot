from aiogram import types
from aiogram.utils import keyboard


class InlineKeyboards:
    def __init__(self) -> None:
        self.keyboard = types.InlineKeyboardMarkup
        self.button = types.InlineKeyboardButton
