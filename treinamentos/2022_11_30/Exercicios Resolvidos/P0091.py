N, M = map(int, input().split())
lista = []
nomes = []
escolhidos = []
for i in range(M):
    nome, idade, A, B, C, D = input().split()
    idade, A, B, C, D = int(idade), int(A), int(B), int(C), int(D)
    lista.append([max([A, B, C]), sum([C, D]), idade, i])
    nomes.append(nome)
lista.sort(reverse=True)
c = 0
for i in range(4):
    if lista[0][i] == lista[1][i]:
        c += 1
if c == 3 and lista[1][3] == 0:
    escolhidos.append(nomes[lista[1][3]]) 
    escolhidos.append(nomes[lista[0][3]])
else:
    escolhidos.append(nomes[lista[0][3]]) 
    escolhidos.append(nomes[lista[1][3]])
if N == 1:
    print(escolhidos[0])
else:
    for i in range(2, N):
        escolhidos.append(nomes[lista[i][3]])
    for i in range(len(escolhidos)):
        print(escolhidos[i])