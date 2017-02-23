import telebot
import telegram_bot_config
import acrcloud_api
import parsing


def listener(messages):
    for m in messages:
        if m.content_type == 'voice':
            file_id = m.voice.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            downloaded_file = bot.download_file(file_path)
            index = str(file_id)
            inputFile = ("%s" % (telegram_bot_config.audio_dir))
            try:
                with open(inputFile, "wb") as new_file:
                    new_file.write(downloaded_file)
                    music_file_path = 'demo.ogg'
                    responce = acrcloud_api.get_responce(config=acrcloud_api.config, music_file_path=music_file_path,
                                                         start_seconds=3)
                    title, artist = acrcloud_api.parce_responce(responce)
                    if title is None and artist is None:
                        pattern_string = "Увы, я не нашел:("
                        bot.send_message(m.chat.id, pattern_string)
                    else:
                        yandex_music_ref = parsing.get_ref(title, artist)
                        pattern_string = "Это песня " + title + " исполнителя " + artist + "!\n" + "Ссылка на Яндекс.Музыку " + yandex_music_ref
                        bot.send_message(m.chat.id, pattern_string)

            except NameError:
                pass


if __name__ == '__main__':
    bot = telebot.TeleBot(telegram_bot_config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
