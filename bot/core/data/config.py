from utils.get_envs import Environs


class BotConfig:
    BOT_TOKEN: str = Environs.get("TELEGRAM_BOT_TOKEN")
    DRAGO_CONTRACT_ADDRESS: str = Environs.get("DRAGO_CONTRACT_ADDRESS")
    DRAGO_TELEGRAM_CHANNEL_ID_RU: str = Environs.get("DRAGO_TELEGRAM_CHANNEL_ID_RU")
    DRAGO_TELEGRAM_CHAT_ID_RU: str = Environs.get("DRAGO_TELEGRAM_CHAT_ID_RU")
    DRAGO_TELEGRAM_CHANNEL_ID_EN: str = Environs.get("DRAGO_TELEGRAM_CHANNEL_ID_EN")
    DRAGO_TELEGRAM_CHAT_ID_EN: str = Environs.get("DRAGO_TELEGRAM_CHAT_ID_EN")
