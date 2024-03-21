import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\weather_app\gui")
import main_gui
from random import choice

fake_user_agent = [
    "qwer1", "abjdisf3", "1wesdfv3fc", "f28ewgui", "3g9fweguhi",
    "asgtp42pm", "b92euoeomd0", "fg943euniwdq", "29dbe1", "8gewidmq230", 
    "db9uwijdn", "d9id031wdl", "qw2pio412e4ui1r7g", "adoiwo030fnie",
    "f8euniwmod", "g29eiowlda", "dv2bwiqkosld", "sagd9buiwq340"
]

header = {'user-agent': choice(fake_user_agent)}

link = f"https://world-weather.ru/pogoda/russia/moscow/7days/"
req_date = requests.get(link, headers = header)

soup = BeautifulSoup(req_date.content, 'lxml')

info_city = soup.find('h2', class_ = "day-night-city").text[0:-11] # Название города и инфа маленькая

def parse_weather(name_date_parse: str, date_num: int): #name_date_parse = temperature, feeling, wind, humidity. date_num от 0 до 3
    global soup
    global req_date
    parse_value = soup.find_all('td', class_ = f"weather-{name_date_parse}")[date_num].get_text(strip=True)
    return parse_value

print(parse_weather("feeling", 3))
