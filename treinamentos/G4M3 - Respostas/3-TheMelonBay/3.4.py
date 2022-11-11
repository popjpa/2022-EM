from collections import deque

fila = deque()
while True:
    nomes = input()
    if nomes == "FIM":
        break
    elif nomes == "PROXIMO":
        print(f"PROXIMO: {fila.popleft()}")
    else:
        fila.append(nomes)
        print("FILA:", end=' ')
        for i in fila:
            print(f'{i}', end=' ')
        print()