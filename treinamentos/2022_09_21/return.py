def pares(lista):
    lista_pares = [i for i in lista if i % 2 == 0]
    '''for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
        '''
    return lista_pares

lista = [0, 1, 2, 4, 5, 10, 20, 31, 79, 89, 100]
a = pares(lista)
print(a)