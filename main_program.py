## здесь соберем все воедино
import acrcloud_api
import vk_api

# авторизовываемся в вк
api = vk_api.authorization(access_token=vk_api.access_token)

# получаем путь к файлу от алексы...

#но пока стандартный
music_file_path = '/Users/akupriyanov/Desktop/icon_hack/englishman.mp3'

# обрабатываем его через acrcloud_api
responce = acrcloud_api.get_responce(config=acrcloud_api.config, music_file_path=music_file_path, start_seconds=3)
title, artist = acrcloud_api.parce_responce(responce)

# отправляем шаблонную строку в вк
pattern_string = "Это песня " + title + " исполнителя " + artist + "!"
# еще хз как выбирать юзера, поэтому отправляю себе
vk_api.send_message(api=api, user_id=62811131, message=pattern_string)