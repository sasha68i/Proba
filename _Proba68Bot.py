import requests
import datetime
#512171365:AAG16Iv1tcKM7dThUayYZSf42YMHec8Va0Y


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
    
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.get(self.api_url + method, params)
        return resp

    def main():
        update_id = last_update(get_updates_json(url))['uodate_id']
        while True:
            if update_id == last_update(get_updates_json(url))['update_id']:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
                update_id += 1
            sleep(1)


my_bot = BotHandler(token)


def main():
    new_offset = None
    
    while True:
        my_bot.get_updates(new_offset)

        last_update = my_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        my_bot.sennd_message(last_chat_id, "MyTest testing... {}".format(last_chat_name))

        new_offset = last_chat_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()