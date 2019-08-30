import math
y = int(input())
for x in range(y):
    n = int(input())
    aux = 0
    z = 1
    while( math.floor(n/pow(5,z)) >= 1):
        aux = aux + math.floor(n/pow(5,z))
        z = z +1
    print(aux)