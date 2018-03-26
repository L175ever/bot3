import requests
import datetime
import pytz
import pickle


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

        #  def translate (self, token2):
        #     self.token2 = token2

    #    self.api_url2 = "https://translate.yandex.net/api/v1.5/tr.json/translate"


    def get_updates(self, offset=None, timeout=5):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update


token = "441518222:AAFSlYWYs7hMdj0S_w6fOIZuR76rFY1D5uY"
greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
url2 = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = "trnsl.1.1.20180326T062919Z.624758ec4c2a0d50.42091bb8d35300c5d5ba7da719db0b925d79ab36"
lang = 'ru-en'
# now = datetime.datetime.now()
utc_now = pytz.utc.localize(datetime.datetime.utcnow())
now = utc_now.astimezone(pytz.timezone("Europe/Moscow"))
print(now)


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()
        if not last_update:
            continue
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        #s = dict(neskvi = '166965975')
        # загружаем словарь из файла
        with open('dump.dat', 'rb') as dump_in:
            der = pickle.load(dump_in)

        requestpost = requests.post(url2, data={'key': key, 'text': last_chat_text, 'lang': lang})
        response_data = requestpost.json()
        text = last_chat_text
        print('id chat',last_chat_id, ' ', last_chat_name)

        if last_chat_id == 166965975:
            greet_bot.send_message(505269223, '{}'.format(response_data['text'][0]))
        ##            today += 1

        elif now.day == today:

            greet_bot.send_message(166965975, '{}'.format(response_data['text'][0]))

        new_offset = last_update_id + 1
        last_chat_id = str(last_chat_id)
        last_chat_name = str(last_chat_name)
       # f = open('text.txt', 'a')
        #f.write(last_chat_id)
        #f.write(last_chat_name)
        #f.close()
        #запись юзеров в словарь, постоянно стирается((
        # s[last_chat_name] = last_chat_id
        #print(s)
        der[last_chat_name] = last_chat_id

        # снова сохраняем словарь в файл
        with open('dump.dat', 'wb') as dump_out:
            pickle.dump(der, dump_out)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()