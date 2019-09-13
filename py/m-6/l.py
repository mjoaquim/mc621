
import math
y = int(input())
for x in range(y):
    row = input().split(" ")
    a = int(row[0])
    b = int(row[1])
    p = a % 10
    q = b % 4
    if(b == 0):
        print(1)
    elif( p == 1 | p == 2 | p==5 | p==6 ):
        print(p)
    elif (q == 1):
        print(p)
    elif (q == 2):
         print(pow(p,2)%10)
    elif (q == 3):
        print(pow(p,3)%10%10)
    elif (q == 0):
         print(pow(p,4)%10%10%10)