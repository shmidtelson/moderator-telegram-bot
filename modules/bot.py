from settings import BOT_TOKEN
import telegram

from src.utils import BotMeta


class Bot(metaclass=BotMeta):
    def __init__(self):
        self.dispatcher = telegram.Bot(token=BOT_TOKEN)