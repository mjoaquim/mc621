import numpy

fibonacci_numbers = [0, 1]
for i in range(2,60):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

n = int(input())
for x in range(n):
    row = input()
    if int(row) > 5:
        posicao = int(fibonacci_numbers.index(int(row)))
        print(str(fibonacci_numbers[posicao-4]) + " " + str(fibonacci_numbers[posicao-3]) +" " + str(fibonacci_numbers[posicao-1]))
    else:
        print("impossible")
    
