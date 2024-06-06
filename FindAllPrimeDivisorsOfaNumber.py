def countOfDivisors(num):
    count=1
    countOfPrimeDivisor=1
    for i in range(1, num):
        if(num % i == 0):
            for j in range(i):
                if (i % j == 0):
                    countOfPrimeDivisor+=1
            # count = count + 1
    return countOfPrimeDivisor

countDivisorForHighestNumber=0
j=0
d=dict()
while j < 10:
    currentInput = int(input())
    countDividersForCurrentInput = countOfDivisors(currentInput)
    if countDividersForCurrentInput > countDivisorForHighestNumber:
        countDivisorForHighestNumber = countDividersForCurrentInput
        num = currentInput
    elif countDividersForCurrentInput == countDivisorForHighestNumber:
        num = currentInput
    j+=1

print(str(num)+" "+str(countDivisorForHighestNumber))