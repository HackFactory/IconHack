import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

page_pattern = "https://music.yandex.ru"

class PARSERYANDEXMUSIC:
    page_pattern = "https://music.yandex.ru/search?text="

    def __init__(self, title, artist, driver_path='/Users/Roman/Desktop/Git/icon_hack/chromedriver'): # адрес в твоем ноуте
        title = title.replace(" ","%20")
        title = title.lower()
        self.title = title

        artist = artist.replace(" ", "%20")
        artist = artist.lower()
        self.artist = artist

        self.page = self.page_pattern+self.artist+"%20"+self.title
        #print("https://music.yandex.ru/search?text=arctic%20monkeys%20do%20i%20wanna%20know ")
        #print(self.page)
        self.driver_path = driver_path

    def get_browser(self):
        browser = webdriver.Chrome(executable_path=self.driver_path)
        #print("I open: ", self.page)
        browser.get(self.page)
        return browser

    def run(self):
        browser = self.get_browser()
        ref = self.parse(browser)
        browser.close()
        return ref

    def parse(self, browser):
        soup = BeautifulSoup(browser.page_source, "lxml")
        schedule = soup.find_all(class_="track__name-wrap")
        return schedule


def get_ref(title, artist):
    parser = PARSERYANDEXMUSIC(title=title, artist=artist)
    array_of_songs = parser.run()
    if len(array_of_songs) == 0:
        return -1
    else:
        song = array_of_songs[0]
        song = str(song)
        start = song.find("/album")
        end = song.find("\" title")
        ref = song[start:end]
        return page_pattern+ref

#print(get_ref(title="do i wanna know", artist="arctic monkeys"))
