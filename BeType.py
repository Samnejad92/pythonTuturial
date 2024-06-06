string=list(input())
resultList=[]

for i in string:
    if i=='=' and len(resultList) != 0:
        resultList.pop()
    elif i != '=':
        resultList.append(i)
    pass
print(''.join(resultList))