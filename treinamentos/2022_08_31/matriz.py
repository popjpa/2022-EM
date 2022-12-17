matriz = []
for i in range(3):
    matriz.append(['x'] * 3)

for i in range(3):
    for j in range(3):
        matriz[i][j] = input(f'Digite o elemento [{i}][{j}]: ')