from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from datetime import timedelta
from datetime import date
import xlsxwriter



workbook = xlsxwriter.Workbook('yayin_akislari.xlsx')
workbook.formats[0].set_font_size(8)



worksheet = workbook.add_worksheet("Star Yayin Akisi")

URL = 'https://www.startv.com.tr/yayin-akisi'

worksheet.write(0, 0, "STAR")
worksheet.write("A2", "OPT")
worksheet.write("A9", "PT Haber")
worksheet.write("A10", "PT-1")
worksheet.write("A11", "PT-2")
chromedriver = 'C:/Users/kadir/chromedriver.exe'
service1 = Service(chromedriver)
driver = webdriver.Chrome(service=service1)
driver.get(URL)
time.sleep(1)


star_yayin_gunler = []
html1 = driver.page_source
soup = BeautifulSoup(html1, 'html.parser')
gun_linkler = soup.find_all('div', attrs={'class': ['col-md-1 col-xs-4', 'col-md-1 col-xs-4 active is-selected']})
for gun in gun_linkler:
    test = gun.a.get('href')
    star_yayin_gunler.append('https://www.startv.com.tr'+test)
column = 0
for i in star_yayin_gunler:
    URL = i
    driver.get(URL)
    html1 = driver.page_source
    soup = BeautifulSoup(html1, 'html.parser')
    programlar = soup.find_all('li', attrs={'class': ['col-md-6 col-xs-6 col-sm-6 col-lg-4', 'col-md-6 col-xs-6 col-sm-6 col-lg-4 reverse-card']})
    column += 1
    row = 1
    for program in programlar:
        ara = program.find('h5')
        a = " ".join(ara.get_text().split())
        if a == 'STAR HABER':
            row = 8
        worksheet.write(row, column, a)
        row += 1
        print(a)

worksheet.write(0,0,"SHOW")
worksheet.write(0,1,"Pazartesi")
worksheet.write(0,2,"Sali")
worksheet.write(0,3,"Carsamba")
worksheet.write(0,4,"Persembe")
worksheet.write(0,5,"Cuma")
worksheet.write(0,6,"Cumartesi")
worksheet.write(0,7,"Pazar")

workbook.close()

