from PyQt5 import QtWidgets
from main_gui import Ui_MainWindow
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice

fake_user_agent = [
    "qwer1", "abjdisf3", "1wesdfv3fc", "f28ewgui", "3g9fweguhi",
    "asgtp42pm", "b92euoeomd0", "fg943euniwdq", "29dbe1", "8gewidmq230", 
    "db9uwijdn", "d9id031wdl", "qw2pio412e4ui1r7g", "adoiwo030fnie",
    "f8euniwmod", "g29eiowlda", "dv2bwiqkosld", "sagd9buiwq340"
]

def click_button(
    lineEdit, info_city, 
    temp_1, temp_2, temp_3, temp_4, 
    fill_1, fill_2, fill_3, fill_4,
    wet_1, wet_2, wet_3, wet_4,
    brezee_1, brezee_2, brezee_3, brezee_4
    ):
    try:
        global fake_user_agent
        
        city = lineEdit.text()

        header = {'user-agent': choice(fake_user_agent)}
        link = f"https://world-weather.ru/pogoda/russia/{city}/7days/"
        
        req_date = requests.get(link, headers = header)
        soup = BeautifulSoup(req_date.content, 'lxml')
        
        info_city.setText(soup.find('h2', class_ = "day-night-city").text[0:-11])


        def parse_weather(name_date_parse: str, date_num: int): #name_date_parse = temperature, feeling, wind, humidity. date_num от 0 до 3
            parse_value = soup.find_all('td', class_ = f"weather-{name_date_parse}")[date_num].get_text(strip=True)
            return parse_value

        temp_list = [temp_1, temp_2, temp_3, temp_4]
        flag_count = 0
        for x in temp_list:
            x.setText(parse_weather("temperature", flag_count))
            flag_count += 1
        
        fill_list = [fill_1, fill_2, fill_3, fill_4]
        flag_count = 0
        for x in fill_list:
            x.setText(parse_weather("feeling", flag_count))
            flag_count += 1
        
        wet_list = [wet_1, wet_2, wet_3, wet_4]
        flag_count = 0
        for x in wet_list:
            x.setText(parse_weather("wind", flag_count))
            flag_count += 1
        
        brezee_list = [brezee_1, brezee_2, brezee_3, brezee_4]
        flag_count = 0
        for x in brezee_list:
            x.setText(parse_weather("humidity", flag_count))
            flag_count += 1
    except:
        info_city.setText("Неправильно указано имя города")

