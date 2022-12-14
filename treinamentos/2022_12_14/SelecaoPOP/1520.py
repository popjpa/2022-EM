l = []
while True:
    try:
        n = int(input())
        for i in range(n):
            x, y = map(int, input().split())
            for j in range(x, y+1):
                l.append(j)
        l.sort()
        num = int(input())
        numeros = []
        for i in range(len(l)):
            if l[i] == num:
                numeros.append(i)
        if len(numeros) > 0:
            print(f'{num} found from {numeros[0]} to {numeros.pop()}')
        else:
            print(f'{num} not found')
        l.clear()
    except EOFError:
        break
    except:
        continue