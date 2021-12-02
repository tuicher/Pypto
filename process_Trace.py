import csv
import matplotlib.pyplot as plt

class process_Trace():
    def __init__(self, r):
        self.route = r
        with open(self.route) as file:
            self.it = []
            self.values  = []
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.it.append(int(row[0]))
                self.values.append(float(row[1]))

    def plot(self):
            plt.plot(self.it, self.values, lw=1)
            plt.show()

    def inv(self):
         with open(self.route) as file:




#plot('data/training_traces/down_trace.csv')
#plot('data/training_traces/up_trace.csv')

z = process_Trace('data/training_traces/up_trace.csv')
z.plot()

