import csv
import matplotlib.pyplot as plt
from random import seed
from random import randint

data = ['data/0.5-2400_Data/data_sniff_1_BTCBUSD.csv','data/0.5-2400_Data/data_sniff_2_BTCBUSD.csv','data/0.5-2400_Data/data_sniff_3_BTCBUSD.csv','data/0.5-2400_Data/data_sniff_4_BTCBUSD.csv' ,'data/0.5-2400_Data/data_sniff_5_BTCBUSD.csv']

def getMean(route):
    with open(route) as file:
        reader = csv.reader(file, delimiter=',')
        a = 0
        b =  0
        for row in reader:
            a += 1
            b += float(row[3])
    return b/a

def get_m50(route):
    with open(route) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            return

def plot(route):
    with open(route) as file:
        it = []
        value = []
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            it.append(int(row[0]) + 1)
            value.append(float(row[3]))
            #b = value[::-1]
        plt.plot(it, value)
        plt.show()

def min(list):
    min = 999999999999999999
    for ele in list:
        if(ele < min):
            min = ele
    return min

def max(list):
    max = -1
    for ele in list:
        if(ele > max):
            max = ele
    return max

size_of_Trace = 30
size_of_Slice = 2400

def generate_Trace(file_Route):
    it = []
    values = []
    values_aux = []
    counter = 0
    fix = 0
    seed()
    #for i in range(randint(25,50)):
    #30 iters == 6 hours
    for i in range(size_of_Trace):
        seed()
        pick = randint(0,4)
        print('Pick->', pick)
        with open(data[pick]) as file:
            reader = csv.reader(file, delimiter=',')
            values_aux = []
            for row in reader:
                it.append(counter)
                counter += 1
                values_aux.append(float(row[3]))
                seed()
            if randint(0,1) == 1:
                print(i,'Reversed')
                values_aux.reverse()
            if i!= 0:
                a = values.pop()
                values.append(a)
                fix = values_aux[0] - a
                for ele in values_aux:
                    values.append(ele - fix)
            else:
                values.extend(values_aux)
            
    file = open(file_Route,"a")
    for i in it:
        file.write(str(i) + ',' + str(values[i]) + '\n')
    file.close()
    plt.plot(it,values, lw=1)
    mi = min(values)
    ma = max(values)
    for i in range(size_of_Trace + 1):
        plt.plot([size_of_Slice * i, size_of_Slice * i],[mi, ma], 'k-', lw=0.25)
    plt.show()

generate_Trace('traces/trace1.csv')
