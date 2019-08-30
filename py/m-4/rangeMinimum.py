n = int(input())
row = input().split(" ")
queries = int(input())
for x in range(queries):
    n = input().split(" ")
    a = int(n[0])
    b = int(n[1])
    if(a <= b):
        b = b + 1
        v = row[a:b]
    else: 
        a = a + 1
        v = row[b:a]
    print(str(min(v)))
