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

temperature_night = str(soup.find_all('td', class_ = "weather-temperature")[0])[91:-12] 
temperature_morning = str(soup.find_all('td', class_ = "weather-temperature")[1])[91:-12] 
temperature_day = str(soup.find_all('td', class_ = "weather-temperature")[2])[112:-12] 
temperature_evening = str(soup.find_all('td', class_ = "weather-temperature")[3])[91:-12] 

print(temperature_night)
print(temperature_morning)
print(temperature_day)
print(temperature_evening)
