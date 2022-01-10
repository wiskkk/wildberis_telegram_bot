import json
import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE goods (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
brand TEXT NOT NULL,
name TEXT NOT NULL);""")


def wildberries_request(item_number):
    response = requests.get(f'https://www.wildberries.ru/catalog/{item_number}/detail.aspx?targetUrl=XS')
    soup = BeautifulSoup(response.text, 'lxml')
    brand = soup.find('h1', class_='same-part-kt__header').contents[0].text
    name = soup.find('h1', class_='same-part-kt__header').contents[2].text
    dict_js = {
        'brand': brand,
        'name': name
    }
    js = json.dumps(dict_js, ensure_ascii=False)

    try:
        cursor.execute("""INSERT INTO goods
        VALUES (?,?,?)""", [id(dict_js), dict_js['brand'], dict_js['name']])
    except sqlite3.Error as error:
        print(error)

    return js


wildberries_request(38567378)
