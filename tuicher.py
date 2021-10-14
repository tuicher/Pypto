from binance.client import Client
import config

client = Client(config.API_KEY, config.API_SECRET, testnet=True)

info = client.get_symbol_info('BNBBTC')

prices = client.get_all_tickers()

for s in prices:
    print (s['symbol'], s['price'])

#print(prices)