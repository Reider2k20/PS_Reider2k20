import sqlite3
import requests
from bs4 import BeautifulSoup

connection = sqlite3.connect("Dz_10_weather_1.sl3", 5)
cur = connection.cursor()
try:
    cur.execute("CREATE TABLE first_table (name TEXT);")
except sqlite3.OperationalError:
    pass

cur.execute(f"SELECT rowid, name FROM first_table WHERE rowid={5};")
res = cur.fetchall()
print(res)


cur.execute(f"SELECT rowid, name FROM first_table WHERE rowid=1;")
res = cur.fetchall()
if res == []:
    cur.execute("INSERT INTO first_table (name) VALUES (' ');")
cur.execute(f"SELECT rowid, name FROM first_table WHERE rowid=2;")
res = cur.fetchall()
if res == []:
    cur.execute("INSERT INTO first_table (name) VALUES (' ');")




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


cur.execute(f"UPDATE first_table SET name='{date}: {time}' WHERE rowid=1;")
cur.execute(f"UPDATE first_table SET name='{temperature}' WHERE rowid=2;")

connection.commit()

connection.close()