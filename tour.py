sound = "aeiou"
S = input().lower()
for i in S:
    if i in sound:
        S = S.replace(i, '')

print(''.join('.'+ i for i in S))