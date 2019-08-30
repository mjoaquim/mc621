import math

def contaDigitos(n):
    digitos = 0
    if(n == 1):
        return 1
    digitos = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0)) # formula de Kamenetsky   
    return (math.floor(digitos) + 1)

y = int(input())
for x in range(y):
    n = int(input())
    if(n >= 0):
        print(contaDigitos(n))