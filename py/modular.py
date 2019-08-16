import numpy

n = int(input())
for x in range(n):
    row = input().split(" ")
    b = int(row[0])
    e = int(row[1])
    m = int(row[2])
    calculate = pow(b,e,m)
    print(str(x+1) + ". " + str(calculate))