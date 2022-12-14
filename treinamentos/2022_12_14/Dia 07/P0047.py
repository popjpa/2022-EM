N = int(input())
cont = 0
lista = []
for i in range(1, N+1):
    for j in range(1, i):
        for k in range(1, j):
            if i ** 2 == j ** 2 + k ** 2:
                lista.append([k,j,i])
                cont += 1
lista.sort()
for i in range(len(lista)):
    print(*(lista[i]))

if cont == 0:
    print('nenhuma tripla')