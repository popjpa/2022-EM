contador = 0
N = int(input())
matriz = []
for i in range(N):
    matriz.append(list(input()))
for i in range(N):
    for j in range(N):
        if matriz[i][j] == '*':
            matriz[i][j] = 9
        elif matriz[i][j] == '-':
            matriz[i][j] = 0
for linha in range(N):
    for coluna in range(N):
        if matriz[linha][coluna] != 9:
            qtde = 0
            for i in range(-1 ,2):
                for j in range(-1, 2):
                    if (linha + i >= 0) and (linha + i < N):
                        if (coluna + j >= 0) and (coluna + j < N):
                            if matriz[linha + i][coluna + j] == 9:
                                qtde += 1
            matriz[linha][coluna] = qtde

for i in range(N):
    for j in range(N):
        print(matriz[i][j], end='')
    print()