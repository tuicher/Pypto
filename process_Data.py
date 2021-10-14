import csv

def getMean(route):
    with open(route) as file:
        reader = csv.reader(file, delimiter=',')
        a = 0
        b =  0
        for row in reader:
            a += 1
            b += float(row[3])
        mean = b / a
    return b/a