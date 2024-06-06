import math
x=int(input())
radX = math.radians(x)
print(math.gcd(math.ceil((math.pow(x,5/3)+math.tan(radX))),math.floor(math.pow(math.pi,2+math.atan(math.pow(math.sin(radX),2))))))