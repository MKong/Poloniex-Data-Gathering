#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
beginningOf2016 = 1451566801
beginningOf2017 = 1483189200
requestTicker = requests.get("https://poloniex.com/public?command=returnTicker", verify=False)
dataTicker = requestTicker.json()
index = 0
for itemTicker in dataTicker:
    startHour = 1483146000
    EndHour = 1483189200
    highestPrice = 0
    lowestPrice = 999999.99
    highestTrade = {}
    lowestTrade = {}
    numberTrades = 0
    totalVolumeTraded = 0
    lastTrade = {}
    lastTradeRate = 0
    index = index + 1
    currency_pair = itemTicker
    print(index)
    print(currency_pair)
    if (("USDT" in itemTicker or "BTC" in itemTicker) and (index >43)):
        while (startHour >= beginningOf2016):
                url = "https://poloniex.com/public?command=returnTradeHistory&currencyPair="+currency_pair+"&start="+str(startHour)+"&end="+str(EndHour)
                try:
                    r = requests.get(url, verify=False)
                    data = r.json()
                    for item in data:
                        if(lastTradeRate ==0):
                            lastTradeRate = item["rate"]
                            lastTrade = item
                        if (float(highestPrice) < float(item["rate"])):
                            highestTrade = item
                            highestPrice = float(item["rate"])
                        if (float(lowestPrice) > float(item["rate"])):
                            lowestTrade = item
                            lowestPrice = float(item["rate"])
                        totalVolumeTraded += float(item["amount"])
                        numberTrades +=1
                    EndHour = EndHour - 43200
                    startHour = startHour - 43200
                except Exception as e:
                    print(e)
                    continue
    if (("USDT" in itemTicker or "BTC" in itemTicker) and (index >43)):
        listOne = [currency_pair, highestTrade["rate"], lowestTrade["rate"], lastTradeRate, totalVolumeTraded, numberTrades, highestTrade, lowestTrade, lastTrade ]
        with open("taxonomy_economics.csv", "a") as fp:
          wr = csv.writer(fp, dialect='excel')
          wr.writerow(listOne)
