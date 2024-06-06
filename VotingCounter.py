user_dict = {} 
num_entries = int(input())
lst = []
for i in range(num_entries):
    ele = input()
    lst.append(ele)
    if lst[i] in user_dict.keys():
        user_dict[lst[i]] +=1
    else:
        user_dict[lst[i]] =1
sortedDict = dict( sorted(user_dict.items(), key=lambda x: x[0].lower()) )
for key,value in sortedDict.items():
    print(key," ",value)