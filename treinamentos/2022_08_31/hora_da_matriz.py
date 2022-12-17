matriz = []
N, M = map(int, input().split())
for i in range(N):
    matriz.append(input())
for linha in range(M):
    for coluna in range(N):
        print(matriz[coluna][linha],end='')
    print()