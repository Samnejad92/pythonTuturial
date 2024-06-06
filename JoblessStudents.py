import re
def solve(arr):
    l = re.split(r" \+ | = ", arr)
    hash_index = -1
    
    for i in l:
        if re.search(r'#', i):
            hash_index = l.index(i)
            break

    if hash_index == -1:
        return '-1'
    
    if hash_index == 0:
        dif = int(l[2]) - int(l[1])
        a = l[0].replace('#', '.*')
        accuracy = re.fullmatch(a, str(dif))
        if accuracy:
            return arr.replace(l[0], str(dif))
        else:
            return '-1'

    elif hash_index == 1:
        dif = int(l[2]) - int(l[0])
        a = l[1].replace('#', '.*')
        accuracy = re.fullmatch(a, str(dif))
        if accuracy:
            return arr.replace(l[1], str(dif))
        else:
            return '-1'

    elif hash_index == 2:
        dif = int(l[0]) + int(l[1])
        a = l[2].replace('#', '.*')
        accuracy = re.fullmatch(a, str(dif))
        if accuracy:
            return arr.replace(l[2], str(dif))
        else:
            return '-1'
print(solve("12 + 13 = #6"))
print(solve("10# + 50 = 10052"))
print(solve("15 + 1#2 = 136"))
print(solve("52979783 + 40838457 = #40"))