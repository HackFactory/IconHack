#sudo pip install vk
import vk
import os
import time


# я зарегистрировал бота и получил для него уникальный токен, через который есть полный доступ к его страничке
# через апишку
# login: +7 9102953174
# password: icon_hack
session = vk.Session(access_token='7ed035e2cbd922d9facfd285942094f88ec7edc81a54c318546e328520b28b0136d9aa765b14109e71351')
api = vk.API(session)


time.sleep(1)

# пишем сообщение
api.messages.send(user_id=109876568, message='это сообщение отправлено через api vk на python :)')