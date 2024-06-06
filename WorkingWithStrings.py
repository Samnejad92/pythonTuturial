sample_string='AaEeiIoOUu'
a = input()
for letter in a :
    if letter in sample_string:
        a = a.replace(letter, '.')
print(a.lower())