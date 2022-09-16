from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import lxml

show = ['https://www.showtv.com.tr/yayin-akisi/pazartesi',
        'https://www.showtv.com.tr/yayin-akisi/sali',
        'https://www.showtv.com.tr/yayin-akisi/carsamba',
        'https://www.showtv.com.tr/yayin-akisi/persembe',
        'https://www.showtv.com.tr/yayin-akisi/cuma',
        'https://www.showtv.com.tr/yayin-akisi/cumartesi',
        'https://www.showtv.com.tr/yayin-akisi/pazar']

for i in show:
    show_yayinakisi = i
    get_url = requests.get(show_yayinakisi)
    get_text = get_url.text
    soup = BeautifulSoup(get_text, 'html.parser')

    yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
    oku = ''
    b = 0
    listx = []
    for i in yayinlar:
        a = i.get_text().upper()
        oku = oku + a
        b += 1
        if b % 2 == 0 and b != 0 :
            oku = oku + '\n'

    print(oku)


