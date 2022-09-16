from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from datetime import timedelta
from datetime import date
import xlsxwriter


workbook = xlsxwriter.Workbook('yayin_akislari.xlsx')
workbook.formats[0].set_font_size(8)


worksheet = workbook.add_worksheet("Kanal D Yayin Akisi")


chromedriver = 'C:/Users/kadir/chromedriver.exe'
service1 = Service(chromedriver)
driver = webdriver.Chrome(service=service1)

URL = 'https://www.kanald.com.tr/yayin-akisi'


worksheet.write(0,0,"KANALD")
worksheet.write("A2:A8","OPT")
worksheet.write("A8:A12","PT")
column = 1


driver.get(URL)
time.sleep(1)

html1 = driver.page_source
soup = BeautifulSoup(html1, 'html.parser')
yayingunler = {}
#Aktif günü aramak için
yayinlar2 = soup.find('a', attrs={'class' : 'breadcrumb-link breadcrumb-link-current'})
for aktif_gun in yayinlar2:
    b = " ".join(aktif_gun.get_text().split())
    yayingunler[b] = 'https://www.kanald.com.tr/yayin-akisi'


yayinlar = soup.find('nav', attrs={'class' : 'breadcrumb-sub-nav js-dropdown-list'}).findChildren('li', attrs={'class' : 'breadcrumb-sub-item'})
for yayin_link in yayinlar:
    a = " ".join(yayin_link.get_text().split())
    yayingunler[a] = "https://www.kanald.com.tr/"+yayin_link.a.get("href")

for day in yayingunler:
    URL = yayingunler[day]
    driver.get(URL)
    time.sleep(1)
    html1 = driver.page_source
    soup = BeautifulSoup(html1, 'html.parser')
    yayinlar_son = soup.find('div', attrs={'class': 'schedule-list'}).findChildren('h3', attrs={'class': 'title'})
    print(day)

    if day == 'Pazartesi':
        column = 1
        row = 1
        for i in yayinlar_son:
            yayin_adi = " ".join(i.get_text().split())
            if yayin_adi == "Kanal D Ana Haber" or yayin_adi== 'Kanal D Haber Hafta Sonu':
                row = 7
            worksheet.write(row, column, yayin_adi)
            row += 1
            print(yayin_adi)
    if day == 'Salı':
        column = 2
        row = 1
        for i in yayinlar_son:
            yayin_adi = " ".join(i.get_text().split())
            if yayin_adi == "Kanal D Ana Haber" or yayin_adi== 'Kanal D Haber Hafta Sonu':
                row = 7
            worksheet.write(row, column, yayin_adi)
            row += 1
            print(yayin_adi)
    if day == 'Çarşamba':
        column = 3
        row = 1
        for i in yayinlar_son:
            yayin_adi = " ".join(i.get_text().split())
            if yayin_adi == "Kanal D Ana Haber" or yayin_adi== 'Kanal D Haber Hafta Sonu':
                row = 7
            worksheet.write(row, column, yayin_adi)
            row += 1
            print(yayin_adi)
    if day == 'Perşembe':
        column = 4
        row = 1
        for i in yayinlar_son:
            yayin_adi = " ".join(i.get_text().split())
            if yayin_adi == "Kanal D Ana Haber" or yayin_adi== 'Kanal D Haber Hafta Sonu':
                row = 7
            worksheet.write(row, column, yayin_adi)
            row += 1
            print(yayin_adi)
    if day == 'Cuma':
        column = 5
        row = 1
        for i in yayinlar_son:
            yayin_adi = " ".join(i.get_text().split())
            if yayin_adi == "Kanal D Ana Haber" or yayin_adi== 'Kanal D Haber Hafta Sonu':
                row = 7
            worksheet.write(row, column, yayin_adi)
            row += 1
            print(yayin_adi)
    if day == 'Cumartesi':
        column = 6
        row = 1
        for i in yayinlar_son:
            yayin_adi = " ".join(i.get_text().split())
            if yayin_adi == "Kanal D Ana Haber" or yayin_adi== 'Kanal D Haber Hafta Sonu':
                row = 7
            worksheet.write(row, column, yayin_adi)
            row += 1
            print(yayin_adi)
    if day == 'Pazar':
        column = 7
        row = 1
        for i in yayinlar_son:
            yayin_adi = " ".join(i.get_text().split())
            if yayin_adi == "Kanal D Ana Haber" or yayin_adi== 'Kanal D Haber Hafta Sonu':
                row = 7
            worksheet.write(row, column, yayin_adi)
            row += 1
            print(yayin_adi)

worksheet.write(0,0,"SHOW")
worksheet.write(0,1,"Pazartesi")
worksheet.write(0,2,"Sali")
worksheet.write(0,3,"Carsamba")
worksheet.write(0,4,"Persembe")
worksheet.write(0,5,"Cuma")
worksheet.write(0,6,"Cumartesi")
worksheet.write(0,7,"Pazar")

workbook.close()

