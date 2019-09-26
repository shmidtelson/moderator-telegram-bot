from time import sleep
from modules.bot import Bot

class App:
    def start(self):
        while True:
            print(Bot().dispatcher.get_me())
            sleep(1)
