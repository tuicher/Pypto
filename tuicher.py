# IMPORT SEGMENT
from binance.client import Client
import  time
import config

# BOT ATRIBUTES
PING_RATE = 0.5         
CURRENCY = 'BTCBUSD'
CYCLE_ITERS = 999999    #1x10^6 iteractions * 10 segs = 115 Days

# Variables
val = 0
last_val = 0

client = Client(config.API_KEY, config.API_SECRET, tld='com')

def getData(key):
    #client.ping()
    prices = client.get_all_tickers()
    for s in prices:
        if(s['symbol'] ==  key):
            return s

#Debug
def printAllData():
    client.ping()
    prices = client.get_all_tickers()
    for p in prices:
        print(p['symbol'],': ', p['price'])


#info = client.get_symbol_info('BNBBTC')

i = 0
while i < CYCLE_ITERS:
    value = getData(CURRENCY)

    last_val =  val
    val =  float(value['price'])

    if (last_val > val):
        k = '-'
    else:
        k = '+'

    print(i,'\t', time.ctime(), value['symbol'],': ', value['price'], k, abs(last_val - val))
    i+=1
    time.sleep(PING_RATE)


#print(prices)