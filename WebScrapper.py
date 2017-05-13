import requests
from bs4 import BeautifulSoup as B_soup
import time
value, item = None, None
site = 'http://backpack.tf'
items = {}
go = False

scrapTimes = input('Would you like to run forever? [y/n]:')
if scrapTimes == 'y':
    go = True

while True:
    page = requests.get(site)
    print(page)
    siteCode = B_soup(page.content)
    #print(siteCode)
    price = True
    for i in siteCode.find_all('ul',{'class':'item-list'}):
        for m in i.find_all('span'):
            if price:
                value = m.text
                price = False
            else:
                item = m.text
                items[item] = value
                price = True
    for thing in items.keys():
        print(f'There is a {thing} going for{items[thing]}')
    if not go:
        break   #It's not perfect, but it does the job meh, its a start though. Hope you enjoyed! File in description!
    time.sleep(5)