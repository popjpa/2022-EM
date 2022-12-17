from collections import deque
while True:
    n = int(input())
    if n == 0:
        break
    fila_1 = deque()
    for i in range(1,n+1):
        fila_1.append(i)
    fila_2 = deque()
    while (len(fila_1) > 1):
        fila_2.append(fila_1.popleft())
        fila_1.append(fila_1.popleft())
    cartas_fora = ', '.join([str(i) for i in fila_2])
    print(f'Discarded cards: {cartas_fora}')
    print(f'Remaining card: {fila_1[0]}')
    cartas_fora = ''