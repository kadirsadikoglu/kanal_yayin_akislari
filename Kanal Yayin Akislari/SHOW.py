from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from datetime import timedelta
from datetime import date
import xlsxwriter

show = ['https://www.showtv.com.tr/yayin-akisi/pazartesi',
        'https://www.showtv.com.tr/yayin-akisi/sali',
        'https://www.showtv.com.tr/yayin-akisi/carsamba',
        'https://www.showtv.com.tr/yayin-akisi/persembe',
        'https://www.showtv.com.tr/yayin-akisi/cuma',
        'https://www.showtv.com.tr/yayin-akisi/cumartesi',
        'https://www.showtv.com.tr/yayin-akisi/pazar']


workbook = xlsxwriter.Workbook('yayin_akislari.xlsx')
workbook.formats[0].set_font_size(8)
worksheet = workbook.add_worksheet("Show Yayin Akisi")
worksheet = workbook.add_worksheet("atv Yayin Akisi")


chromedriver = 'C:/Users/kadir/chromedriver.exe'
service1 = Service(chromedriver)
driver = webdriver.Chrome(service=service1)

worksheet.write(0,0,"SHOW")
worksheet.write(0,1,"Pazartesi")
worksheet.write(0,2,"Sali")
worksheet.write(0,3,"Carsamba")
worksheet.write(0,4,"Persembe")
worksheet.write(0,5,"Cuma")
worksheet.write(0,6,"Cumartesi")
worksheet.write(0,7,"Pazar")
worksheet.write("A2:A8","OPT")
worksheet.write("A8","PT Haber")
worksheet.write("A9","PT-1")
worksheet.write("A10","PT-2")
column = 1

for i in show:
    URL = i
    driver.get(URL)

    html1 = driver.page_source
    soup = BeautifulSoup(html1, 'lxml')
    yayinlar = soup.find('div', {'class': ['right-content']}).findChildren('span', {'class': ['title']})
    row = 1
    for i in yayinlar:
        a = " ".join(i.get_text().upper().split())
        if a == "SHOW ANA HABER" or a == "HAFTA SONU ANA HABER":
            row = 7
        worksheet.write(row, column, a)
        row += 1
        print(a)
    column += 1


workbook.close()

