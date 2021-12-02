import pandas as pd

class Pypto():
    def __init__(self):
        self.valorList = []

    def iterate(self, valor):
        self.actualValor = valor
        self.valorList.insert(0, valor)
        self.checkMeans()

    def setM50(self):
        self.mFifty = self.meanN(50)

    def meanN(self, n):
        i = 0
        mean = 0
        while i < n:
            mean += self.valorList[i]
            i += 1
        return mean / n
    
    def checkMeans(self):
        if len(self.valorList) >= 50:
            self.setM50()


route = "data/training_traces/up_trace.csv"
size_Trace = 250

with open(route) as infile:
    lines = pd.read_csv(infile, nrows=size_Trace)
    for index, row in lines.interrows():
        print("a")
