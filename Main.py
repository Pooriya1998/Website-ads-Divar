from bs4 import BeautifulSoup
import requests
import re

page = requests.get('https://divar.ir/s/isfahan')

soup = BeautifulSoup(page.content, 'html.parser')

l = list()
car_name = soup.find_all("div", class_="kt-post-card__body")
for i in range(0,len(car_name)):
    l.append(car_name[i])

li_a = list()
li_a1 = list()
for i in range(0,len(l)):
    a = l[i].find('div', class_="kt-post-card__title")
    a = list(a)
    a = a[0]

    a1 = l[i].find('div', class_="kt-post-card__description")
    if a1 != None:
        a1 = list(a1)
        a1 = a1[0]

        li_a.append(a)
        li_a1.append(a1)

for i in range(0,len(li_a)):
    if "توافقی" == li_a1[i]:
        print(li_a[i],':',li_a1[i])
