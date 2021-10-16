import csv
import matplotlib.pyplot as plt

def plot(route):
    with open(route) as file:
        it = []
        values  = []
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            it.append(int(row[0]))
            values.append(float(row[1]))

        plt.plot(it, values, lw=1)
        plt.show()

#plot('data/training_traces/down_trace.csv')
#plot('data/training_traces/up_trace.csv')
plot('traces/DEMO_trace.csv')