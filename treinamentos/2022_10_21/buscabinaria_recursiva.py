import time
def busca_binaria(lista, inicio, fim, valor):
    if inicio <= fim:
        meio = (inicio + fim) // 2
        if valor > lista[meio]:
            return busca_binaria(lista, meio+1, fim, valor)
        elif valor < lista[meio]:
            return busca_binaria(lista, inicio, meio-1, valor)
        else:       
            return meio
    return -1

lista = list(range(2000000, -1, -1))
ini2 = time.time()
lista.sort()
print(busca_binaria(lista, 0, len(lista)-1, len(lista)-1))
fim2 = time.time()
total = (fim2 - ini2)
print(f"Tempo: {total:.2f} ms")