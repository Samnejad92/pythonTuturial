a=list()
i=0
while(True):
    a.append(int(input()))
    if(a[i] == 0):
        break
    i = i+1
a.pop()
a.reverse()    
for num in a:
    print(num)