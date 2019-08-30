s = int(input())
inputA = int(str(s),2)
aux = 0
pot = 1
while (inputA > pot):
    aux = aux + 1
    pot = pot*4
print(aux)