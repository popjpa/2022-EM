L, C = map(int, input().split())
LR = [0] * L
CR = [0] * C
matriz = []
#inserindo os valores + verificando os locais de deposito
for i in range(L):
    valores = list(map(int, input().split()))
    matriz.append(valores)
    for j in range(C):
        if valores[j] == 1: 
            LR[i] = 1
            CR[j] = 1
#somar os locais que tem depósito
print(LR.count(1) + CR.count(1))
#imprimindo a matriz + M ou - (o * tira os colchetes da matriz)
for i in range(L):
    if LR[i] == 1: 
        print(*(matriz[i]), 'M')
    else: 
        print(*(matriz[i]), '-')
for i in CR:
    if i == 1: 
        print('M', end=' ')
    else: 
        print('-',end=' ')