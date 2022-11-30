import random
def merge(esquerda, direita, lista):
    i, j, k = 0,0,0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
            k += 1
        else:
            lista[k] = direita[j]
            j += 1
            k += 1

    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1
    
    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1

def mergesort(lista):
    if len(lista) < 2:
        return lista
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    mergesort(esquerda)
    mergesort(direita)
    merge(esquerda, direita, lista)

#lista_aleatorios = random.sample(range(1, 1000), 100)
lista_aleatorios = [20, 50, 42, 36, 2, 10, 1, 41]
print('Lista não ordenada ', lista_aleatorios)
print()
mergesort(lista_aleatorios)
print('Lista ordenada: ', lista_aleatorios)