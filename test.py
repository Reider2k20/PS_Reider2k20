import requests
from bs4 import BeautifulSoup

resp = requests.get("https://ua.sinoptik.ua/погода-чернігів")
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features = "html.parser")
    soup_list = soup.find_all('p')
    soup_list = str(soup_list[23]).split('<p class="today-time">Погода сьогодні о ')
    soup_list = str(soup_list[1]).split('</p>')
    time = str(soup_list[0])
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features = "html.parser")
    soup_list = soup.find_all('p')
    soup_list = str(soup_list[24]).split('<p class="today-temp">')
    soup_list = str(soup_list[1]).split('</p>')
    temperature = str(soup_list[0])
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features = "html.parser")
    soup_list = soup.find_all('p')
    soup_list = str(soup_list[2]).split('p class="day-link" data-link="//ua.sinoptik.ua/погода-чернігів/')
    soup_list = str(soup_list[1]).split('">Субота</p>')
    date = str(soup_list[0])
