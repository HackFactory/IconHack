#sudo pip install vk
import vk

# я зарегистрировал бота и получил для него уникальный токен, через который есть полный доступ к его страничке
# через апишку
# login: +7 9102953174
# password: icon_hack

access_token='7ed035e2cbd922d9facfd285942094f88ec7edc81a54c318546e328520b28b0136d9aa765b14109e71351'

def authorization(access_token):
    session = vk.Session(access_token=access_token)
    api = vk.API(session)
    return api

def send_message(api, user_id, message):
    # пишем сообщение
    api.messages.send(user_id=user_id, message=message)

def generate_pattern_string():
    pass