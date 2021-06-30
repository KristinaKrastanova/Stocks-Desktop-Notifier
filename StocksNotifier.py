from get_tickers import*
import string
import yfinance as yf 
from plyer import notification 
from datetime import date
import csv
from csv import writer

def writeStock(file, stock):
    dict = [date.today().strftime("%d/%m/%Y"), stock.info["longName"],stock.info["symbol"]]
    with open(file, 'a+', newline='', encoding='utf-8') as writeObj:
        myWriter = writer(writeObj, delimiter = ";")
        myWriter.writerow(dict)

def notifyUser (stock):
    notification.notify(
            title = "STOCKS ATTENTION",
            message = "Check out {name} for possible spike to the moon!\n".format(
                        name = stock.info["longName"]),  
            app_icon = r'chart-growth.ico',
            timeout  = 10
        )

    writeStock('moonStocks.csv', stock)

def checkConditions(tickersList):
    for i in tickersList:
        try:  
            print("Processing " + i.info["symbol"] + "...") 
            data = i.history(period = "3mo")
            volumes = data['Volume'].tolist()
            average3months = sum(volumes) / len(volumes)    
            first = i.info["marketCap"] < 200000000000
            second = i.info["volume"] > average3months * 2
        except:  
            continue

        if(first and second):
            notifyUser(i)


def main():
    
    for letter in string.ascii_uppercase:
        tickersList = get_tickers(letter)
        checkConditions(tickersList)
    

if __name__ == "__main__":
    main()