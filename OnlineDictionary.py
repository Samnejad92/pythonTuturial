num_entries = int(input())
dict={}
string=''
for i in range(num_entries):
    l1=[str(x) for x in input().split()]
    dict[l1[0]]=l1[1]
str_entries = input().split()
for i in range(len(str_entries)):
    if str_entries[i] in dict :
        string += dict[str_entries[i]] + ' '
    else :
        string += str_entries[i] + ' '
print(string)