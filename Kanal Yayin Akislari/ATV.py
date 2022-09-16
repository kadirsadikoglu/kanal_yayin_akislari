from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from datetime import timedelta
from datetime import date
import xlsxwriter


workbook = xlsxwriter.Workbook('yayin_akislari.xlsx')
workbook.formats[0].set_font_size(8)
worksheet = workbook.add_worksheet("Atv Yayin Akisi")


chromedriver = 'C:/Users/kadir/chromedriver.exe'
service1 = Service(chromedriver)
driver = webdriver.Chrome(service=service1)

URL = 'https://www.atv.com.tr/yayin-akisi'

today = date.today().strftime("%#d/%#m/%Y")
day_check = date.today().strftime("%A")
if day_check == "Monday":
    day_check= "Pazartesi"
elif day_check == "Tuesday":
    day_check = "Sali"
elif day_check == "Wednesday":
    day_check = "Carsamba"
elif day_check == "Thursday":
    day_check = "Persembe"
elif day_check == "Friday":
    day_check = "Cuma"
elif day_check == "Saturday":
    day_check = "Cumartesi"
else:
    day_check = "Pazar"
worksheet.write(0,0,"ATV")
worksheet.write(1,0,"EOPT")
worksheet.write("A3:A8","OPT")
worksheet.write("A9:A12","PT")
column = 1
if day_check == "Pazartesi":
    for i in range(0,7):
        new_day = date.today() + timedelta(days= i)
        new_day2 = new_day.strftime("%A")
        new_day = new_day.strftime("%#d/%#m/%Y")
        print(new_day2)

        driver.get(URL)
        driver.execute_script("changeStreamDay('"+new_day+"')")
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        #yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
        yayinlar = soup.find_all('a', attrs={'class': ['title blankpage']})
        oku = ''
        b = 0
        listx = []
        row = 1
        for i in yayinlar:
            a = " ".join(i.get_text().upper().split())
            if a == "ATV ANA HABER":
                row = 8
            worksheet.write(0,column,new_day2)
            worksheet.write(row,column,a)
            row += 1
            print(a)
        column += 1
elif day_check == "Sali":
    for i in range(0,7):
        new_day = date.today() + timedelta(days= i-1)
        new_day2 = new_day.strftime("%A")
        new_day = new_day.strftime("%#d/%#m/%Y")
        print(new_day2)

        driver.get(URL)
        driver.execute_script("changeStreamDay('"+new_day+"')")
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        #yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
        yayinlar = soup.find_all('a', attrs={'class': ['title blankpage']})
        oku = ''
        b = 0
        listx = []
        row = 1
        for i in yayinlar:
            a = " ".join(i.get_text().upper().split())
            if a == "ATV ANA HABER":
                row = 8
            worksheet.write(0,column,new_day2)
            worksheet.write(row,column,a)
            row += 1
            print(a)
        column += 1
elif day_check == "Carsamba":
    for i in range(0,7):
        new_day = date.today() + timedelta(days= i-2)
        new_day2 = new_day.strftime("%A")
        new_day = new_day.strftime("%#d/%#m/%Y")
        print(new_day2)

        driver.get(URL)
        driver.execute_script("changeStreamDay('"+new_day+"')")
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        #yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
        yayinlar = soup.find_all('a', attrs={'class': ['title blankpage']})
        oku = ''
        b = 0
        listx = []
        row = 1
        for i in yayinlar:
            a = " ".join(i.get_text().upper().split())
            if a == "ATV ANA HABER":
                row = 8
            worksheet.write(0,column,new_day2)
            worksheet.write(row,column,a)
            row += 1
            print(a)
        column += 1
elif day_check == "Persembe":
    for i in range(0,7):
        new_day = date.today() + timedelta(days= i-3)
        new_day2 = new_day.strftime("%A")
        new_day = new_day.strftime("%#d/%#m/%Y")
        print(new_day2)

        driver.get(URL)
        driver.execute_script("changeStreamDay('"+new_day+"')")
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        #yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
        yayinlar = soup.find_all('a', attrs={'class': ['title blankpage']})
        oku = ''
        b = 0
        listx = []
        row = 1
        for i in yayinlar:
            a = " ".join(i.get_text().upper().split())
            if a == "ATV ANA HABER":
                row = 8
            worksheet.write(0,column,new_day2)
            worksheet.write(row,column,a)
            row += 1
            print(a)
        column += 1
elif day_check == "Cuma":
    for i in range(0,7):
        new_day = date.today() + timedelta(days= i-4)
        new_day2 = new_day.strftime("%A")
        new_day = new_day.strftime("%#d/%#m/%Y")
        print(new_day2)

        driver.get(URL)
        driver.execute_script("changeStreamDay('"+new_day+"')")
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        #yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
        yayinlar = soup.find_all('a', attrs={'class': ['title blankpage']})
        oku = ''
        b = 0
        listx = []
        row = 1
        for i in yayinlar:
            a = " ".join(i.get_text().upper().split())
            if a == "ATV ANA HABER":
                row = 8
            worksheet.write(0,column,new_day2)
            worksheet.write(row,column,a)
            row += 1
            print(a)
        column += 1
elif day_check == "Cumartesi":
    for i in range(0,7):
        new_day = date.today() + timedelta(days= i-5)
        new_day2 = new_day.strftime("%A")
        new_day = new_day.strftime("%#d/%#m/%Y")
        print(new_day2)

        driver.get(URL)
        driver.execute_script("changeStreamDay('"+new_day+"')")
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        #yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
        yayinlar = soup.find_all('a', attrs={'class': ['title blankpage']})
        oku = ''
        b = 0
        listx = []
        row = 1
        for i in yayinlar:
            a = " ".join(i.get_text().upper().split())
            if a == "ATV ANA HABER":
                row = 8
            worksheet.write(0,column,new_day2)
            worksheet.write(row,column,a)
            row += 1
            print(a)
        column += 1
elif day_check == "Pazar":
    for i in range(0,7):
        new_day = date.today() + timedelta(days= i-6)
        new_day2 = new_day.strftime("%A")
        new_day = new_day.strftime("%#d/%#m/%Y")
        print(new_day2)

        driver.get(URL)
        driver.execute_script("changeStreamDay('"+new_day+"')")
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        #yayinlar = soup.find_all('a', attrs={'class': ['title blankpage','time blankpage']})
        yayinlar = soup.find_all('a', attrs={'class': ['title blankpage']})
        oku = ''
        b = 0
        listx = []
        row = 1
        for i in yayinlar:
            a = " ".join(i.get_text().upper().split())
            if a == "ATV ANA HABER":
                row = 8
            worksheet.write(0,column,new_day2)
            worksheet.write(row,column,a)
            row += 1
            print(a)
        column += 1
worksheet.write(0,0,"SHOW")
worksheet.write(0,1,"Pazartesi")
worksheet.write(0,2,"Sali")
worksheet.write(0,3,"Carsamba")
worksheet.write(0,4,"Persembe")
worksheet.write(0,5,"Cuma")
worksheet.write(0,6,"Cumartesi")
worksheet.write(0,7,"Pazar")

workbook.close()

