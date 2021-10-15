import process_Data


route = 'data/0.5-2400_Data/data_sniff_3_BTCBUSD.csv'

a =  process_Data.getMean(route)

process_Data.plot(route)

print(a)