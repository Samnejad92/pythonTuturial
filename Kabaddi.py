a=int(input()) 
l1=[int(x) for x in input().split()]
l=[int(y) for y in l1 if y <=2]
print(int(len(l)/3))