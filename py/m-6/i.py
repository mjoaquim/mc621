import math


y = int(input())
aux = 0

if(y == 1):
    print(1)
elif(y < 9):
    cont = math.floor(3*y/2)
    print(cont-1)
else:
    for x in range(1,math.floor(y**(1/2))+1):
            aux = aux + math.floor(y/x) - (x-1)
        
    print(aux)