from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import requests
from datetime import timedelta
from datetime import date
import xlsxwriter



workbook = xlsxwriter.Workbook('yayin_akislari.xlsx')
workbook.formats[0].set_font_size(8)



worksheet = workbook.add_worksheet("TRT1 Yayin Akisi")

URL = 'https://www.trt1.com.tr/yayin-akisi'

worksheet.write("A2", "OPT")
worksheet.write("A9", "PT Haber")
worksheet.write("A10", "PT-1")
worksheet.write("A11", "PT-2")

r = requests.get(URL)
time.sleep(1)

def otomatik_gun(x):
    soup = BeautifulSoup(r.content, 'lxml')
    row = 1
    yayin_akis = soup.find('div', attrs={'id': x}).findChildren('h2', attrs={'class': 'title'})
    list1 = []
    for k in yayin_akis:
        a = k.get_text()
        if a != 'İddiaların Aksine':
            list1.append(a)
    for i in list1:
        if i == "Ana Haber":
            row = 8
        c = " ".join(i.upper().split())
        worksheet.write(row, column, c)
        row += 1


column = 1
otomatik_gun('Pazartesi')
column = 2
otomatik_gun('Salı')
column = 3
otomatik_gun('Çarşamba')
column = 4
otomatik_gun('Perşembe')
column = 5
otomatik_gun('Cuma')
column = 6
otomatik_gun('Cumartesi')
column = 7
otomatik_gun('Pazar')



worksheet.write(0,0,"TRT1")
worksheet.write(0,1,"Pazartesi")
worksheet.write(0,2,"Sali")
worksheet.write(0,3,"Carsamba")
worksheet.write(0,4,"Persembe")
worksheet.write(0,5,"Cuma")
worksheet.write(0,6,"Cumartesi")
worksheet.write(0,7,"Pazar")

workbook.close()

