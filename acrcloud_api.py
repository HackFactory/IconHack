#sudo pip install vk
import vk
# c этим сложнее. https://github.com/acrcloud/acrcloud_sdk_python
# там есть инструкция, только файл setup.py пуст, поэтому нужно в него скопировать содержимое
# файлика //python2.7/setup.py
from acrcloud.recognizer import ACRCloudRecognizer

# конфиг стандартный, я зарегистрировал аккаунт на acrcloud.com
# login: kupriyanovartem@yandex.ru
# password: M4E-HrQ-kCp-MRQ
# интсрукция по заведению нового инстанса есть в мануале на гитхабе, но кажется, нам и с такими ключами хватит

config = {
    # Replace "xxxxxxxx" below with your project's host, access_key and access_secret.
    'host': 'eu-west-1.api.acrcloud.com',
    'access_key': '4aca6d089717c23585f43b957870c8c3',
    'access_secret': '2WM52yeRg7TaizVhlk7RkdA0FVqgp4iVOupE1CM4',
    'timeout': 10  # seconds
}

music_file_path = '/Users/akupriyanov/Desktop/icon_hack/englishman.mp3'

def get_responce(config, music_file_path, start_seconds=3):
    recognizer = ACRCloudRecognizer(config)
    # responce = recognizer.recognize_by_file(file_path='/Users/akupriyanov/Desktop/icon_hack/Oxxxymiron.mp3', start_seconds=3)
    responce = recognizer.recognize_by_file(file_path=music_file_path, start_seconds=start_seconds)
    return responce


def parce_responce(response):
    print(response)
    split_responce = response.split(':')
    arr_responce = []
    for i, element_responce in enumerate(split_responce):
        arr_responce += element_responce.split(',')

    print(arr_responce)
    is_find = True

    for i, element_responce in enumerate(arr_responce):
        if 'msg' in element_responce:
            if 'Success' in arr_responce[i + 1]:
                print("Я нашел и начинаю парсинг!")
                break
            else:
                print("Я не нашел:(")
                is_find = False
                break

    title, artist = None, None

    if is_find:
        for i, element_responce in enumerate(arr_responce):
            if 'title' in element_responce:
                title = arr_responce[i + 1]
                title = ''.join(
                    list(
                        filter(
                            lambda ch: ch not in "?.!/;:\\\"'{[]}", title)
                    )
                )
            if 'artists' in element_responce  and 'name' in arr_responce[i + 1]:
                artist = arr_responce[i + 2]
                artist = ''.join(
                    list(
                        filter(
                            lambda ch: ch not in "?.!/;:\\\"'{[]}", artist)
                    )
                )

    return (title, artist)


print(parce_responce(get_responce(config, music_file_path, 3)))