a = input()
l=list()
b=list()
l=a.split('+')
l=[int(x) for x in l]
l.sort()
list_string_l = map(str, l)
x = "+".join(word for word in list_string_l if int(word) <= 3)
print(x)