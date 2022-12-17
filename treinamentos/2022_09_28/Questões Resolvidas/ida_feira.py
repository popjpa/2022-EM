#Problema 1281 Beecrowd
N = int(input())
dicionario = {}
for i in range(N):
    somador = 0
    M = int(input())
    for j in range(M):
        chave, valor = input().split()
        valor = float(valor)
        dicionario[chave] = valor
    P = int(input())
    for j in range(P):
        chave, valor = input().split()
        valor = int(valor)
        if chave in dicionario.keys():
            somador += (valor * dicionario[chave])
    print(f"R$ {somador:.2f}")
    dicionario.clear()