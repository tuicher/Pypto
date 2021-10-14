# IMPORT SEGMENT
from binance.client import Client
import  time
import config

# BOT ATRIBUTES
PING_RATE = 0.5         
CURRENCY = 'BTCBUSD'
CYCLE_ITERS = 12

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
file = open("data/data.csv","a")
i = 0
while i < CYCLE_ITERS:
    value = getData(CURRENCY)

    last_val =  val
    val =  float(value['price'])

    if (last_val > val):
        k = '-'
    else:
        k = '+'

    print(i, CYCLE_ITERS,'\t', time.ctime(), value['symbol'],': ', value['price'], k, abs(last_val - val))
    file.write(str(i) + ',' + str(time.ctime()) +','+value['symbol']+','+ value['price']+','+str(k)+','+str(abs(last_val - val))+'\n')
    i+=1
    time.sleep(PING_RATE)

file.close
#print(prices)