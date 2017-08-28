import requests
from time import sleep

url = "https://api.telegram.org/bot380121426:AAGvwWxEsmBpdY7IwIS5z2ZQs9ZabZ6_3Uk/"
def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id
def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))

send_mess(chat_id, 'Your message goes here')