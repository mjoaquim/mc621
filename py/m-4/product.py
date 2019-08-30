while True:
    try:
        n1 = int(input())
        n2 = int(input())
        print(str(n1*n2))
    except EOFError:
        break