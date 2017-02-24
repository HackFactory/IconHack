## здесь соберем все воедино
import acrcloud_api
import vk_api
import time
import urllib.request
import os
import parsing

# авторизовываемся в вк
api = vk_api.authorization(access_token=vk_api.access_token)

ts = api.messages.getLongPollServer()['ts']

#ждем новые сообщения
while True:
    time.sleep(5)
    request = api.messages.getLongPollHistory(ts=ts)

    # если есть новые сообщения
    if len(request['messages']) != 1:
        user_id = request['profiles'][0]['uid']
        msg = request['messages'][1]
        message_id = msg['mid']
        # если в этом новом сообщении есть госовое сообщение
        if 'attachments' in msg:
            doc = msg['attachments'][0]['doc']

            #скачиваем голосовой файл
            urllib.request.urlretrieve(doc['url'], str(message_id) + 'responce.mp3')

            #распознаем его
            music_file_path = './' + str(message_id) + 'responce.mp3'
            responce = acrcloud_api.get_responce(config=acrcloud_api.config, music_file_path=music_file_path,
                                                 start_seconds=3)
            #возвращаем ответ
            title, artist = acrcloud_api.parce_responce(responce)
            print(title, artist)
            #если не нашли ответ
            if title is None and artist is None:
                pattern_string = "Увы, я не нашел:("
                vk_api.send_message(api=api, user_id=user_id, message=pattern_string)
            else:
                yandex_music_ref = parsing.get_ref(title, artist)
                if yandex_music_ref == -1: # если песня распозналась, но ее нет в Я.Музыке
                    pattern_string = "Это песня " + title + " исполнителя " + artist + "!\n"
                else:
                    pattern_string = "Это песня " + title + " исполнителя " + artist + "!\n" + "Ссылка на Яндекс.Музыку " + yandex_music_ref
                vk_api.send_message(api=api, user_id=user_id, message=pattern_string)

            os.remove(music_file_path)
        else:
            welcome_string = "Hi! You can send me voice message and i will tell you what song is it :)"
            vk_api.send_message(api=api, user_id=user_id, message=welcome_string)
        api.messages.markAsRead(message_ids=message_id)

    ts = api.messages.getLongPollServer()['ts']