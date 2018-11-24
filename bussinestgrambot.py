import requests
import datetime

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

    def send_message(self, chat_id, text):
        method = 'sendMessage'
        params = {'chat_id': char_id, 'text': text}
        resp = request.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

bot = BotHandler('725747356:AAEFgtOqhV9Wm56U2E2J4QZnqS-kGSd3glg')
greetings = ('здравствуйте', 'привет', 'ку', 'здорово', 'hello')

def main():
    new_offset = None

    last_update = bot.get_last_update()

    last_update_id = last_update['update_id']
    last_text = last_update['message']['text']
    last_id = last_update['message']['chat']['id']
    last_name = last_update['message']['chat']['first_name']

    if last_text.lower() in greetings:
        bot.send_message(last_id, 'Привет, {}'.format(last_name))

    new_offset = last_update_id + 1;

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
