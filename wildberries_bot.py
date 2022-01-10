# 2065112463:AAEdZEB5xVnoApNQAY4UM2FCp2DKl4QJ9Ok
from bs4 import BeautifulSoup
import requests
import telebot

bot = telebot.TeleBot('2065112463:AAEdZEB5xVnoApNQAY4UM2FCp2DKl4QJ9Ok')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'To search for a brand by article, use /get_brand *article*\n'
                                      'To search for a title by article, use /get_title *article*')


@bot.message_handler(commands=['get_brand'])
def get_brand(message):
    try:
        item_number = message.text.split()[-1]
        url = f'https://by.wildberries.ru/catalog/{item_number}/detail.aspx?targetUrl=SP'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        brand = soup.find('h1', class_='same-part-kt__header').contents[0].text
        bot.send_message(message.chat.id, brand)
    except AttributeError:
        bot.send_message(message.chat.id, 'AttributeError, try another article')


@bot.message_handler(commands=['get_title'])
def get_title(message):
    try:
        item_number = message.text.split()[-1]
        url = f'https://by.wildberries.ru/catalog/{item_number}/detail.aspx?targetUrl=SP'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('h1', class_='same-part-kt__header').contents[2].text
        bot.send_message(message.chat.id, title)
    except AttributeError:
        bot.send_message(message.chat.id, 'AttributeError, try another article')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Try using /start to see what functions are available')


bot.polling(none_stop=True, interval=2)
