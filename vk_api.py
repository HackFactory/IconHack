#sudo pip install vk
import vk
import time

# я зарегистрировал бота и получил для него уникальный токен, через который есть полный доступ к его страничке
# через апишку

access_token='**************************************************'

def authorization(access_token):
    session = vk.Session(access_token=access_token)
    api = vk.API(session)
    return api

def send_message(api, user_id, message):
    # пишем сообщение
    api.messages.send(user_id=user_id, message=message)

api = authorization(access_token)
#messages = api.messages.getHistory(user_id=119012868)
#print(messages# )
ts = api.messages.getLongPollServer()['ts']
time.sleep(10)
print(api.messages.getLongPollHistory(ts=ts))