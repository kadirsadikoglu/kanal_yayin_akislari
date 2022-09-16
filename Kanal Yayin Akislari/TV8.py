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

URL = 'https://www.tv8.com.tr/yayin-akisi'

worksheet.write("A2", "OPT")
worksheet.write("A9", "PT-1")


r = requests.get(URL)
time.sleep(1)

soup = BeautifulSoup(r.content, 'lxml')
row = 1
gunler = soup.find('div', attrs={'id': 'hdtb-msb'})
gunler_list = []
for i in gunler:
    gunler_list.append(i.a.get('href'))

def program_cekme(x):
        URL = x
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'lxml')
        row = 1
        print()


        program_adi = soup.find('table', attrs={'class': 'table'})
        for junk in program_adi.find_all('span', attrs={'class': 'stream-type'}):
            junk.extract()

        for z in program_adi.find_all(attrs={'class': 'stream-name'}):
            sorunsuz_ad = " ".join(z.get_text().upper().split())
            if sorunsuz_ad == 'MASTERCHEF TÜRKIYE / YENI BÖLÜM' or sorunsuz_ad == 'MASTERCHEF TÜRKIYE / ÖZET':
                row = 9
            worksheet.write(row, column, sorunsuz_ad)
            row += 1

#for i in gunler_list:
column = 0
for i in gunler_list:
    column += 1
    program_cekme(i)


worksheet.write(0,0,"TV8")
worksheet.write(0,1,"Pazartesi")
worksheet.write(0,2,"Sali")
worksheet.write(0,3,"Carsamba")
worksheet.write(0,4,"Persembe")
worksheet.write(0,5,"Cuma")
worksheet.write(0,6,"Cumartesi")
worksheet.write(0,7,"Pazar")

workbook.close()

