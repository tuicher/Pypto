import csv
import matplotlib.pyplot as plt

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
        plt.plot(it, value)
        plt.show()

