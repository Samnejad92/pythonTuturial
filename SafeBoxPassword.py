k=int(input())
password = input()
countOfMoves=0
for i in range(k):
    roller = input()
    ind = roller.find(password[i])
    if(ind>4):
        ind=9-ind
        countOfMoves+=ind
    else:
        countOfMoves+=ind
print(countOfMoves)