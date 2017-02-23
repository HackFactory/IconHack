#sudo pip install vk
import vk


# я зарегистрировал бота и получил для него уникальный токен, через который есть полный доступ к его страничке
# через апишку
# login: +7 999 8502068
# password: icon_hack
session = vk.Session(access_token='81628d12d01aba9628dc7563b5e0d5d8bbecfef39d419e15bf465aac260a2af4cc18fa5f7d76a1395d464')
api = vk.API(session)

# пишет на стене сообщение
api.wall.post(message = 'Hello, World!')
#profiles = api.users.get(user_id=62811131)
#print(profiles[0]['first_name']+' '+profiles[0]['last_name'])

api.messages.send(user_id=62811131, message='hello!')