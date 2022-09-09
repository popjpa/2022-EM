matriz = []
soma = 0
for i in range(12):
    matriz.append([0] * 12)
linha_operacao = int(input())
operacao = input()
for linha in range(12):
    for coluna in range(12):
        matriz[linha][coluna] = float(input())
soma = sum(matriz[linha_operacao])
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':  
    media = soma / 12 
    print(f'{media:.1f}')