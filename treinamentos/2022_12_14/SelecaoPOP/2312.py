N = int(input())
l = []
nomes = []
for i in range(N):
    nome, ouro, prata, bronze = input().split()
    ouro, prata, bronze = int(ouro), int(prata), int(bronze)
    l.append([ouro, prata, bronze, i])
    nomes.append(nome)
l.sort(reverse=True)
r = []
aux = [None] * N
for i in range(N):
    aux[l[i][3]] = nomes[l[i][3]]
    r.append([aux[l[i][3]]])
    for j in range(3):
        r[i].append(l[i][j])
for i in r:
    print(*i)