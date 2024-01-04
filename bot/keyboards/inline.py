from aiogram import types
from aiogram.utils import keyboard


class InlineKeyboards:
    def __init__(self) -> None:
        self.keyboard = types.InlineKeyboardMarkup
        self.button = types.InlineKeyboardButton

    def new_post_keyboard(self, lang: str = "RU") -> types.InlineKeyboardMarkup:
        buttons = [
            [
                self.button(
                    text="Как купить $DRAGO" if lang == "RU" else "How to buy $DRAGO",
                    url="https://telegra.ph/Kak-kupit-Drago-01-01" if lang == "RU" else "https://telegra.ph/How-to-buy-Drago-12-27",
                ),
            ],
            [
                self.button(
                    text="Сайт" if lang == "RU" else "Site",
                    url="https://drago.network/",
                ),
                self.button(
                    text="Твиттер" if lang == "RU" else "Twitter",
                    url="https://x.com/drago_solana/",
                ),
            ],
            [
                self.button(
                    text="EN Канал" if lang == "RU" else "Our channel",
                    url="https://t.me/dragosol",
                ),
                self.button(
                    text="EN Чат" if lang == "RU" else "Our chat",
                    url="https://t.me/dragosolanachat",
                ),
            ],
            [
                self.button(
                    text="Raydium",
                    url="https://raydium.io/swap/?inputCurrency=sol&outputCurrency=5D9LBmEeWjKXZs8JRaP8YdBDdkdQPwu9mATXTcMUq7YU",
                ),
            ],
            [
                self.button(text="DEX Screener", url="https://dexscreener.com/solana/GD6sCpWTmhmCPHZkza1a7JLNcqER3tuBnY3jqsHzL6v2"),
                self.button(text="Birdeye", url="https://birdeye.so/token/GD6sCpWTmhmCPHZkza1a7JLNcqER3tuBnY3jqsHzL6v2?chain=solana"),
            ],
        ]
        return self.keyboard(inline_keyboard=buttons)