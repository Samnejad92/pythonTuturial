num_entries = int(input())
lst = []
happyIrsaFlag=False
for i in range(num_entries):
    l1=[int(x) for x in input().split()]
    lst.append(l1)
for i in range(len(lst)):
    for j in range(1, len(lst)):
        if lst[i][0] < lst[j][0]:
            if lst[i][1] > lst[j][1]:
                happyIrsaFlag=True
print("happy irsa" if happyIrsaFlag else "poor irsa")