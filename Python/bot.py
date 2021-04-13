import requests
from components import tokendb
from components import movies
from components import bank
from time import sleep

#Бот 

token = tokendb.token
URL = 'https://api.telegram.org/bot' + token + '/'
global last_update_id
last_update_id = 0



def get_updates():
    url = URL + 'getupdates'
    r = requests.get (url)
    return r.json ()



def get_message():
    data = get_updates ()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id, 'text': message_text}

        return message


def get_last_text(message):
    return message['message']['text']
text_element = get_updates()['result']
z = []
for i in text_element:
    print(get_last_text(i))
    y = get_last_text(i)
    z.append(y)
    if len(z) == 5:
        break



def send_message( chat_id, text='Wait, pleasse...' ):
    url = URL + 'sendmessage?chat_id={}&text={}'.format (chat_id, text)
    requests.get (url)


def main():
    while True:
        answer = get_message ()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/movies':
                send_message (chat_id, movies.movies_today)
            if text == '/courses':
                send_message (chat_id, bank.get_money())



        else:
            continue
        sleep (2)


if __name__ == '__main__':
    main ()
