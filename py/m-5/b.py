import numpy

row = input().split(" ")

a = int(row[0])
b = int(row[1])
aux = 1
if(a >= 1):
    if(b >= 2):
        while((a/b) >= 1):
            a = a/b
            aux = aux + 1
        print(aux)
