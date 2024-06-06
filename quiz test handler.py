mak= open('mak.txt')
print(type(mak.readlines()))
print(type(mak.read()))
print(type(mak.readline()))

import csv
with open('input.csv') as f:
    reader = csv.reader(f)
    for i in reader:
        print(type(i))

mRa = 569.34643865
print("result %1.0f" %mRa)