
import math
y = int(input())
row = input().split(" ")
pares = 0
impares = 0
for x in range(y):
    if(int(row[x]) % 2 == 0):
        pares = pares +1
    else:
        impares = impares + 1

if(pares >= impares):
    print(impares)
else:
    print(pares)

    