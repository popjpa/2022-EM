import time
def busca(lista, valor):
    for i in range(len(lista)):
        if (lista[i] == valor):
            return i
    return -1

lista = list(range(2000000, -1, -1))
ini2 = time.time()
lista.sort()
print(busca(lista, len(lista)-1))
fim2 = time.time()
total = (fim2 - ini2)
print(f"Tempo: {total:.2f} ms")