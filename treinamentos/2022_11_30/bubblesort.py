from random import sample

def bubble_sort(vetor):
    trocou = True
    while trocou:
        trocou = False
        for i in range(len(vetor)-1):
            if vetor[i] > vetor[i+1]:
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux
                trocou = True
lista = list(sample(range(1, 20), 10))
#lista = [20, 40, 10, 5, 3, 1, 30, 2]
bubble_sort(lista)
print(lista)