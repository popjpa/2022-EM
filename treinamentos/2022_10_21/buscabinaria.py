import time
def busca_binaria(lista, inicio, fim, valor):
    while inicio <= fim:
        meio = (fim + inicio) // 2
        print(meio)
        if lista[meio] == valor:
            return meio
        elif valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

lista = list(range(0, 20000000))
ini = time.time()
print(busca_binaria(lista, 0, len(lista)-1, len(lista)-1))
fim = time.time()
print(f'Tempo: {(fim - ini):.10f} ms')