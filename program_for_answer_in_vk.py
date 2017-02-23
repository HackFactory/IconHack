## здесь соберем все воедино
import acrcloud_api
import vk_api
import time
import urllib.request

# авторизовываемся в вк
api = vk_api.authorization(access_token=vk_api.access_token)

ts = api.messages.getLongPollServer()['ts']
while True:
    time.sleep(5)
    request = api.messages.getLongPollHistory(ts=ts)

    if len(request['messages']) != 1:
        user_id = request['profiles'][0]['uid']
        msg = request['messages'][1]
        message_id = msg['mid']
        if 'attachments' in msg:
            print(msg['attachments'][0])
            doc = msg['attachments'][0]['doc']
            print(doc)
            print(user_id)
            urllib.request.urlretrieve(doc['url'], 'responce.mp3')
            responce = acrcloud_api.get_responce(config=acrcloud_api.config, music_file_path='./responce.mp3',
                                                 start_seconds=3)
            title, artist = acrcloud_api.parce_responce(responce)
            pattern_string = "Это песня " + title + " исполнителя " + artist + "!"
            vk_api.send_message(api=api, user_id=user_id, message=pattern_string)


        api.messages.markAsRead(message_ids=message_id)

        #download file
        # responce = acrcloud_api.get_responce(config=acrcloud_api.config, music_file_path=music_file_path,
        #                                      start_seconds=3)
        # title, artist = acrcloud_api.parce_responce(responce)
        #
        # # нужно отметить сообщение как прочитанное
        #
        #
        # # отправляем шаблонную строку в вк
        # pattern_string = "Это песня " + title + " исполнителя " + artist + "!"
        # vk_api.send_message(api=api, user_id=user_id, message=pattern_string)

    else:
        print('skip')

    ts = api.messages.getLongPollServer()['ts']