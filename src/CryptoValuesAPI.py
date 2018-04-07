import pandas as pd
import requests
import time
import os, sys
from random import randint
from pytrends.request import TrendReq
from datetime import datetime

class CryptoValuesFetcher():
    def __init__(self):
        req = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()
        info = req['Data']
        self.coinlist = pd.DataFrame(info).transpose()

    def getHistDay(self, end, days, save=False):
        self.end = end
        self.days = days
        missingcoins = []
        fullPriceData = pd.DataFrame()
        for coin in self.coinlist['Name']:
            try:
                req = requests.get('https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym=USD&limit={}&toTs={}'.format(coin, days, end)).json()
                info = req['Data']
                priceData = pd.DataFrame(info)
                priceData.insert(0, 'coin', coin)
                fullPriceData = fullPriceData.append(priceData, ignore_index=True)
            except:
                print('unable to fetch {} price data').format(coin)
                missingcoins += [coin]
                pass

        if save:
            save_path = os.path.abspath(os.path.join('../data'))
            file = '{}/PriceList_{}_{}'.format(save_path, datetime.fromtimestamp(end).strftime('%m%d%y'), days)
            fullPriceData.to_csv(file, index=False)

        return fullPriceData


