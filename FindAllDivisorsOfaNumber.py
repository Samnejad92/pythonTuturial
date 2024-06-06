def countOfDivisors(num):
    count = 1
    for i in range(1, num):
        if num % i == 0:
            count = count + 1
    return count


countDivisorForHighestNumber = 0
num = 0
j = 0
while j < 20:
    currentInput = int(input())
    countDividersForCurrentInput = countOfDivisors(currentInput)
    if countDividersForCurrentInput > countDivisorForHighestNumber:
        countDivisorForHighestNumber = countDividersForCurrentInput
        num = currentInput
    elif (
        countDividersForCurrentInput == countDivisorForHighestNumber
        and currentInput > num
    ):
        num = currentInput
    j += 1

print(str(num) + " " + str(countDivisorForHighestNumber))