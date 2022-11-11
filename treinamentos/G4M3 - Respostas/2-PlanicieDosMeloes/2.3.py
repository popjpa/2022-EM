N = int(input())
lista = []
for i in range(N):
    nomes = input()
    if nomes not in lista:
        lista.append(nomes)
    else:
        pass
for i in lista:
    print(i)