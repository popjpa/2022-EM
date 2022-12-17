def selection_sort(vetor):
    for i in range(len(vetor)):
        pos_menor = i
        menor = vetor[i]
        for j in range(i+1, len(vetor)):
            if vetor[j] < menor:
                menor = vetor[j]
                pos_menor = j
        vetor[pos_menor] = vetor[i]
        vetor[i] = menor

lista = [50, 20, 10, 30, 40, 80, 50]
selection_sort(lista)
print(lista)