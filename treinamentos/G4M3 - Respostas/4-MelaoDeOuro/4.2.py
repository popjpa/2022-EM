N = int(input())
matriz = []
count_1 = count_2 = count_3 = 0
for i in range(N):
    matriz.append([0] * N)
for i in range(N):
    matriz[i] = input().split()
    matriz[i] = list(map(int, matriz[i]))
for i in range(N):
    for j in range(N):
        if matriz[i][j] <= 90:
            matriz[i][j] = '+'
            count_1 += 1
        elif matriz[i][j] > 90 and matriz[i][j] <= 100:
            matriz[i][j] = 'o'
            count_2 += 1
        else:
            matriz[i][j] = '-'
            count_3 += 1
for i in range(N):
    for j in range(N):
        print(matriz[i][j], end='')
    print()
print()
print(f'+: {count_1}')
print(f'o: {count_2}')
print(f'-: {count_3}')