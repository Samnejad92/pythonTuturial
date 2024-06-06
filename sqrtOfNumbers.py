import math

k = int(input())
l = list()

for i in range(k):
    number = f"{math.sqrt(int(input())):1.8f}"
    l.append(number)
for j in l:
    print(j[:-4])