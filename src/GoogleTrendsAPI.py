from pytrends.request import TrendReq
import requests
import pandas as pd
import os, sys
import time
from datetime import datetime

class GoogleTrendsFetcher():
    def __init__(self):
        req = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()
        info = req['Data']
        self.coinlist = pd.DataFrame(info).transpose()
        self.CryptoTrend = TrendReq()

    def crypto_trends_fetcher(self, start, end, batch_size=500, sleep=3, missing=False, save=False):
        coins = list(self.coinlist['CoinName'])
        if missing:
            coins = self.missingcoins.copy()

        missingcoins = []
        batch_start = 0
        batch_end = min(len(coins), batch_size)
        AllCoinTrends = pd.DataFrame()

        while batch_start < len(coins):
            CoinTrends = pd.DataFrame()
            for coin in coins[batch_start: batch_end]:
                try:
                    time.sleep(sleep) #Request at most 1 time per second to avoid request limits
                    self.CryptoTrend.build_payload(kw_list=[coin], timeframe='{} {}'.format(start, end))
                    interest_coin = self.CryptoTrend.interest_over_time()
                    interest_coin.rename(columns = {coin : 'interest'}, inplace = True)
                    interest_coin.insert(0, 'CoinName', coin)
                    CoinTrends = CoinTrends.append(interest_coin)
                except:
                    print('unable to fetch {} price data'.format(coin))
                    missingcoins += [coin]
                    pass

            AllCoinTrends = AllCoinTrends.append(CoinTrends)

            batch_start += batch_size
            batch_end = min(len(coins), batch_start + batch_size)
            time.sleep(60)

        self.missingcoins = missingcoins
        AllCoinTrends = AllCoinTrends.reset_index().merge(self.coinlist[['CoinName', 'Name']], on=['CoinName']).set_index('index')

        if save:
            save_path = os.path.abspath(os.path.join('../data'))
            file = '{}/CryptoTrends_{}_{}'.format(save_path, start, end)
            AllCoinTrends.to_csv(file, index=False)

        return AllCoinTrends


    # # Request the trends data for each list
    # trends1 = CoinInterest(coins1, start, end)
    # trends2 = CoinInterest(coins2, start, end)
    # trends3 = CoinInterest(coins3, start, end)
    # missing = list(set(coins1)-set(trends1.coin))
    # missing += list(set(coins2)-set(trends2.coin))
    # missing += list(set(coins3)-set(trends3.coin))
    # trendsMiss = CoinInterest(missing, start, end)
    # missing2 = list(set(missing)-set(trendsMiss.coin))
    # trendsMiss2 = CoinInterest(missing2, start, end)
    # missing3 = list(set(missing2)-set(trendsMiss2.coin))


    # # Merge data together and save
    # AllCoinTrends = pd.DataFrame()
    # AllCoinTrends = AllCoinTrends.append([trends1, trends2, trends3, trendsMiss, trendsMiss2])
    # AllCoinTrends = AllCoinTrends.reset_index().merge(coinList[['CoinName', 'Name']], left_on=['coin'], right_on=['CoinName']).set_index('index')
    # del AllCoinTrends['coin']

    # # Not all coins seem to be covered by the algorithm, could be due to the coins with star behind their Name??
    # AllCoinTrends.to_csv('CoinTrends.csv')