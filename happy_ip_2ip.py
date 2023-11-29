# импорт библиотеки requests
import requests

# импорт библиотеки BeautifulSoup
from bs4 import BeautifulSoup

# импорт встроенной библиотеки для открытия страниц в браузере
import webbrowser

# URL страницы для запроса
happy_ip_url = 'https://2ip.ru/happy-ip/'

# GET-запрос к ресурсу и результат ответа сохраняем в переменной response
response = requests.get(happy_ip_url, headers={'User-Agent': 'Mozilla/5.0'})

# Создаём объект BeautifulSoup, указывая html-парсер
page = BeautifulSoup(response.text, 'lxml')
# page = BeautifulSoup(response.text, 'html.parser')

# print(response.text)

# выводим статус ip на текущий момент
print(ip_status:=page.find('div', class_='page_happy_ip__result_usual').text.strip())
# Стандартный ответ (блоки a, b, c, d для ipv4): Ваш IP адрес: aaa.bbb.ccc.ddd — обычный

# если статус не "обычный", а "счастливый", то 
# открываем новую вкладку - страницу регистрации на 2ip.ru без приглашения
if ip_status.split()[-1] != 'обычный':
    print('Ура! Регистрируемся без приглашения на 2ip.ru')
    webbrowser.open_new_tab(reg_url='https://2ip.ru/registration/')