import math
y = int(input())
for x in range(y):
    contador = 0
    n = int(input())
    row = input().split(" ")
    if(n == 1):
        print("0")
    else:
        minimo = int(row[n-1])
        for y in reversed(row):
            if(int(y) > minimo):
                contador = contador + 1
            else:
                minimo = int(y)
        print(contador)
    