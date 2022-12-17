meio_linha = meio_coluna = 2
matriz = []
for i in range(5):
    matriz.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if matriz[i][j] == 1:
            pos_linha = i
            pos_coluna = j
qntd_movimento = abs(pos_linha - meio_linha) + abs(pos_coluna - meio_coluna)
print(qntd_movimento)