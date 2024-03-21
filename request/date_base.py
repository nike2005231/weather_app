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

link = f"https://world-weather.ru/pogoda/russia/rostov_na_donu/7days/"
req_date = requests.get(link, headers = header)

soup = BeautifulSoup(req_date.content, 'lxml')

info_city = soup.find('h2', class_ = "day-night-city").text[0:-11] # Название города и инфа маленькая

temperature_night = soup.find_all('td', class_ = "weather-temperature")[0].get_text(strip=True)
temperature_morning = soup.find_all('td', class_ = "weather-temperature")[1].get_text(strip=True)
temperature_day = soup.find_all('td', class_ = "weather-temperature")[2].get_text(strip=True)
temperature_evening = soup.find_all('td', class_ = "weather-temperature")[3].get_text(strip=True)

filling_night = soup.find_all('td', class_ = "weather-feeling")[0].get_text(strip=True)
filling_morning = soup.find_all('td', class_ = "weather-feeling")[1].get_text(strip=True)
filling_day = soup.find_all('td', class_ = "weather-feeling")[2].get_text(strip=True)
filling_evening = soup.find_all('td', class_ = "weather-feeling")[3].get_text(strip=True)

brezee_night = soup.find_all('td', class_ = "weather-wind")[0].get_text(strip=True)
brezee_morning = soup.find_all('td', class_ = "weather-wind")[1].get_text(strip=True)
brezee_day = soup.find_all('td', class_ = "weather-wind")[2].get_text(strip=True)
brezee_evening = soup.find_all('td', class_ = "weather-wind")[3].get_text(strip=True)

print(brezee_night)
print(brezee_morning)
print(brezee_day)
print(brezee_evening)
