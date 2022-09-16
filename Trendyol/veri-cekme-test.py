from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import requests
from datetime import timedelta
from datetime import date
import xlsxwriter



URL = 'https://www.trendyol.com/tum-saglik-urunleri-mega-eylul/butikdetay/612627'



r = requests.get(URL)

soup = BeautifulSoup(r.content, 'lxml')
gunler = soup.find_all('span', attrs={'class': 'brand'})
print(gunler)

