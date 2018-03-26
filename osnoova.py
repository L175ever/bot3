import requests
import datetime
import pytz
import pickle

token = "412796748:AAGsTvRM2PnmVKEk3dxjEObT566hSzWi7gI"
url2 = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = "trnsl.1.1.20180326T062919Z.624758ec4c2a0d50.42091bb8d35300c5d5ba7da719db0b925d79ab36"
lang = 'ru-en'

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

greet_bot = BotHandler(token)

def