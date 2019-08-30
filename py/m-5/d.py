import numpy

def powerset(s):
    soma = 0
    x = len(s)
    for i in range(1 << x):
        d = ([s[j] for j in range(x) if (i & (1 << j))])
        sum = 0
        for i in range(len(d)):
            sum = (int(d[i]) | sum)
        soma = sum + soma
    return soma

n = int(input())
if(n>=1 & n<=20):
    row = input().split(" ")
    aux = powerset(row)
    print(str(aux))