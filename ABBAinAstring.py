word = input()
if word.find('AB') != -1:
    y = word.replace('AB','', 1)
    if y.find('BA') != -1:
        print("YES")
    else:
        print("NO")