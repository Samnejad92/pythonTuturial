inp=input().lower()
he=list()
for i in inp:
    if i in 'hello' and i not in he:
        he.append(i)
        print(i)