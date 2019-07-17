
# Little scraper version 0.1

# Author Mykola Prokopenko


import requests
import bs4
import time

def parcePrice():
    r=requests.get('https://finance.yahoo.com/quote/FB/')
    soup=bs4.BeautifulSoup(r.text,"xml")
    priceFB=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return priceFB

while True:
    print('The current price: '+str(parcePrice()))
    time.sleep(60)
