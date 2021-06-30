import requests
from bs4 import BeautifulSoup
import yfinance as yf

def findThem(rows):
    list = []
    for i in rows:
        name = i.find_all('td')[0].text.strip()
        if("Fund" in name or "Trust" in name):
            continue
        list.append(yf.Ticker(i.find_all('td')[1].text.strip()))
    return list

def get_tickers(letter):
    URL1 =  'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies='+ letter
    page1 = requests.get(URL1)
    soup1 = BeautifulSoup(page1.text, "html.parser")
    oddRows1 = soup1.find_all('tr', attrs= {'class':'ts0'})
    evenRows1 = soup1.find_all('tr', attrs= {'class':'ts1'})

    URL2 =  'https://www.advfn.com/nasdaq/nasdaq.asp?companies='+ letter
    page2 = requests.get(URL2)
    soup2 = BeautifulSoup(page2.text, "html.parser")
    oddRows2 = soup2.find_all('tr', attrs= {'class':'ts0'})
    evenRows2 = soup2.find_all('tr', attrs= {'class':'ts1'})

    return (findThem(oddRows1) + findThem(evenRows1) + findThem(oddRows2) + findThem(evenRows2))



