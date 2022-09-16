from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from datetime import timedelta
from datetime import date
import xlsxwriter
import requests

Kanallar = ['ATV','SHOW','KANALD','STAR','TRT1','TV8']

workbook = xlsxwriter.Workbook('yayin_akislari.xlsx')
workbook.formats[0].set_font_size(8)

for i in Kanallar:
    if i == 'ATV':
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
        worksheet.write("A2","OPT")
        worksheet.write("A9","PT Haber")
        worksheet.write("A10", "PT-1")
        worksheet.write("A11", "PT-2")
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
        worksheet.write(0,0,"ATV")
        worksheet.write(0,1,"Pazartesi")
        worksheet.write(0,2,"Sali")
        worksheet.write(0,3,"Carsamba")
        worksheet.write(0,4,"Persembe")
        worksheet.write(0,5,"Cuma")
        worksheet.write(0,6,"Cumartesi")
        worksheet.write(0,7,"Pazar")
    elif i == 'SHOW':
        show = ['https://www.showtv.com.tr/yayin-akisi/pazartesi',
                'https://www.showtv.com.tr/yayin-akisi/sali',
                'https://www.showtv.com.tr/yayin-akisi/carsamba',
                'https://www.showtv.com.tr/yayin-akisi/persembe',
                'https://www.showtv.com.tr/yayin-akisi/cuma',
                'https://www.showtv.com.tr/yayin-akisi/cumartesi',
                'https://www.showtv.com.tr/yayin-akisi/pazar']

        worksheet = workbook.add_worksheet("Show Yayin Akisi")

        chromedriver = 'C:/Users/kadir/chromedriver.exe'
        service1 = Service(chromedriver)
        driver = webdriver.Chrome(service=service1)

        worksheet.write(0, 0, "SHOW")
        worksheet.write(0, 1, "Pazartesi")
        worksheet.write(0, 2, "Sali")
        worksheet.write(0, 3, "Carsamba")
        worksheet.write(0, 4, "Persembe")
        worksheet.write(0, 5, "Cuma")
        worksheet.write(0, 6, "Cumartesi")
        worksheet.write(0, 7, "Pazar")
        worksheet.write("A2:A8", "OPT")
        worksheet.write("A8", "PT Haber")
        worksheet.write("A9", "PT-1")
        worksheet.write("A10", "PT-2")
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
    elif i == 'KANALD':
        worksheet = workbook.add_worksheet("Kanal D Yayin Akisi")

        chromedriver = 'C:/Users/kadir/chromedriver.exe'
        service1 = Service(chromedriver)
        driver = webdriver.Chrome(service=service1)

        URL = 'https://www.kanald.com.tr/yayin-akisi'

        worksheet.write(0, 0, "KANALD")
        worksheet.write("A2:A8", "OPT")
        worksheet.write("A8", "PT Haber")
        worksheet.write("A9", "PT-1")
        worksheet.write("A10", "PT-2")
        column = 1

        driver.get(URL)
        time.sleep(1)

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        yayingunler = {}
        # Aktif günü aramak için
        yayinlar2 = soup.find('a', attrs={'class': 'breadcrumb-link breadcrumb-link-current'})
        for aktif_gun in yayinlar2:
            b = " ".join(aktif_gun.get_text().split())
            yayingunler[b] = 'https://www.kanald.com.tr/yayin-akisi'

        yayinlar = soup.find('nav', attrs={'class': 'breadcrumb-sub-nav js-dropdown-list'}).findChildren('li', attrs={
            'class': 'breadcrumb-sub-item'})
        for yayin_link in yayinlar:
            a = " ".join(yayin_link.get_text().split())
            yayingunler[a] = "https://www.kanald.com.tr/" + yayin_link.a.get("href")

        for day in yayingunler:
            URL = yayingunler[day]
            driver.get(URL)
            time.sleep(1)
            html1 = driver.page_source
            soup = BeautifulSoup(html1, 'html.parser')
            yayinlar_son = soup.find('div', attrs={'class': 'schedule-list'}).findChildren('h3',
                                                                                           attrs={'class': 'title'})
            print(day)

            if day == 'Pazartesi':
                column = 1
                row = 1
                for i in yayinlar_son:
                    yayin_adi = " ".join(i.get_text().split())
                    if yayin_adi == "Kanal D Ana Haber" or yayin_adi == 'Kanal D Haber Hafta Sonu':
                        row = 7
                    worksheet.write(row, column, yayin_adi)
                    row += 1
                    print(yayin_adi)
            if day == 'Salı':
                column = 2
                row = 1
                for i in yayinlar_son:
                    yayin_adi = " ".join(i.get_text().split())
                    if yayin_adi == "Kanal D Ana Haber" or yayin_adi == 'Kanal D Haber Hafta Sonu':
                        row = 7
                    worksheet.write(row, column, yayin_adi)
                    row += 1
                    print(yayin_adi)
            if day == 'Çarşamba':
                column = 3
                row = 1
                for i in yayinlar_son:
                    yayin_adi = " ".join(i.get_text().split())
                    if yayin_adi == "Kanal D Ana Haber" or yayin_adi == 'Kanal D Haber Hafta Sonu':
                        row = 7
                    worksheet.write(row, column, yayin_adi)
                    row += 1
                    print(yayin_adi)
            if day == 'Perşembe':
                column = 4
                row = 1
                for i in yayinlar_son:
                    yayin_adi = " ".join(i.get_text().split())
                    if yayin_adi == "Kanal D Ana Haber" or yayin_adi == 'Kanal D Haber Hafta Sonu':
                        row = 7
                    worksheet.write(row, column, yayin_adi)
                    row += 1
                    print(yayin_adi)
            if day == 'Cuma':
                column = 5
                row = 1
                for i in yayinlar_son:
                    yayin_adi = " ".join(i.get_text().split())
                    if yayin_adi == "Kanal D Ana Haber" or yayin_adi == 'Kanal D Haber Hafta Sonu':
                        row = 7
                    worksheet.write(row, column, yayin_adi)
                    row += 1
                    print(yayin_adi)
            if day == 'Cumartesi':
                column = 6
                row = 1
                for i in yayinlar_son:
                    yayin_adi = " ".join(i.get_text().split())
                    if yayin_adi == "Kanal D Ana Haber" or yayin_adi == 'Kanal D Haber Hafta Sonu':
                        row = 7
                    worksheet.write(row, column, yayin_adi)
                    row += 1
                    print(yayin_adi)
            if day == 'Pazar':
                column = 7
                row = 1
                for i in yayinlar_son:
                    yayin_adi = " ".join(i.get_text().split())
                    if yayin_adi == "Kanal D Ana Haber" or yayin_adi == 'Kanal D Haber Hafta Sonu':
                        row = 7
                    worksheet.write(row, column, yayin_adi)
                    row += 1
                    print(yayin_adi)

        worksheet.write(0, 0, "KANAL D")
        worksheet.write(0, 1, "Pazartesi")
        worksheet.write(0, 2, "Sali")
        worksheet.write(0, 3, "Carsamba")
        worksheet.write(0, 4, "Persembe")
        worksheet.write(0, 5, "Cuma")
        worksheet.write(0, 6, "Cumartesi")
        worksheet.write(0, 7, "Pazar")
    elif i == 'STAR':
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
        gun_linkler = soup.find_all('div',
                                    attrs={'class': ['col-md-1 col-xs-4', 'col-md-1 col-xs-4 active is-selected']})
        for gun in gun_linkler:
            test = gun.a.get('href')
            star_yayin_gunler.append('https://www.startv.com.tr' + test)
        column = 0
        for i in star_yayin_gunler:
            URL = i
            driver.get(URL)
            html1 = driver.page_source
            soup = BeautifulSoup(html1, 'html.parser')
            programlar = soup.find_all('li', attrs={
                'class': ['col-md-6 col-xs-6 col-sm-6 col-lg-4', 'col-md-6 col-xs-6 col-sm-6 col-lg-4 reverse-card']})
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

        worksheet.write(0, 0, "STAR")
        worksheet.write(0, 1, "Pazartesi")
        worksheet.write(0, 2, "Sali")
        worksheet.write(0, 3, "Carsamba")
        worksheet.write(0, 4, "Persembe")
        worksheet.write(0, 5, "Cuma")
        worksheet.write(0, 6, "Cumartesi")
        worksheet.write(0, 7, "Pazar")
    elif i == 'TRT1':
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

        worksheet.write(0, 0, "TRT1")
        worksheet.write(0, 1, "Pazartesi")
        worksheet.write(0, 2, "Sali")
        worksheet.write(0, 3, "Carsamba")
        worksheet.write(0, 4, "Persembe")
        worksheet.write(0, 5, "Cuma")
        worksheet.write(0, 6, "Cumartesi")
        worksheet.write(0, 7, "Pazar")
    elif i == 'TV8':
        worksheet = workbook.add_worksheet("TV8 Yayin Akisi")

        URL = 'https://www.tv8.com.tr/yayin-akisi'

        worksheet.write("A2", "OPT")
        worksheet.write("A10", "PT-1")

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


        # for i in gunler_list:
        column = 0
        for i in gunler_list:
            column += 1
            program_cekme(i)

        worksheet.write(0, 0, "TV8")
        worksheet.write(0, 1, "Pazartesi")
        worksheet.write(0, 2, "Sali")
        worksheet.write(0, 3, "Carsamba")
        worksheet.write(0, 4, "Persembe")
        worksheet.write(0, 5, "Cuma")
        worksheet.write(0, 6, "Cumartesi")
        worksheet.write(0, 7, "Pazar")

workbook.close()

