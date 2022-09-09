matriz = []
for i in range(12):
    matriz.append([0] * 12)
coluna_operacao = int(input())
operacao = input()
soma = 0
for linha in range(12):
    for coluna in range(12):
        matriz[linha][coluna] = float(input())
        if coluna == coluna_operacao:
            soma += matriz[linha][coluna]
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    media = soma / 12
    print(f'{media:.1f}')