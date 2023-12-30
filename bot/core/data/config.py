from utils.get_envs import Environs


class BotConfig:
    BOT_TOKEN: str = Environs.get("TELEGRAM_BOT_TOKEN")
    DRAGO_CONTRACT_ADDRESS: str = Environs.get("DRAGO_CONTRACT_ADDRESS")
