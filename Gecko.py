import pandas as pd
from pycoingecko import CoinGeckoAPI
import json
from datetime import date


cg = CoinGeckoAPI()

def trending ():    
    top = cg.get_search_trending()
    df = pd.json_normalize(top, record_path=['coins'])
    df['Date'] = date.today().strftime("%d/%m/%Y")
    
    return df


def market_data (pagee):
    markets = cg.get_coins_markets('USD', per_page = 250, page = pagee, price_change_percentage = ['24h','7d'])
    ef = pd.DataFrame(markets)
    ef['Date'] = date.today().strftime("%d/%m/%Y")
    return ef


def get_all_market (no_pages) : 
    start = 1
    stop = no_pages + 1
    df = pd.DataFrame()
    
    for pagee in range(start,stop):
        ef = market_data(pagee)
        df = df.append(ef)
    
    cf = df.reset_index(drop = True)
    
    return cf



if __name__ == '__main__':
    ''''print(trending())
    print(get_all_market(4).head())
    



