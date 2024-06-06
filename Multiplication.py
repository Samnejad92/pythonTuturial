# n = int(input("Enter number: ")) 
# for i in range(1, n + 1): 
#     for x in range(1, n + 1):
#         print(i * x, end=" ")
#     print()
grade = {'mahdi':20 , 'amin':15 ,'keyvan':19 ,'behzad':11}
z = list(grade.items())
z[1] = ('raha',15)
print(z[1])