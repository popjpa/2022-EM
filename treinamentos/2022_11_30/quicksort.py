import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [i for i in lista if i < pivo]
    iguais = [i for i in lista if i == pivo]
    maiores = [i for i in lista if i > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

#lista_aleatorios = random.sample(range(1, 1000), 100)
lista_aleatorios = [4, 7, 2, 6, 4, 1, 8, 3]
print('Lista não ordenada ', lista_aleatorios)
print()
print(f'Lista ordenada: ', quicksort(lista_aleatorios))
