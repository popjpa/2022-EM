lista = []
while True:
    nomes = input()
    if nomes == 'FIM':
        break
    lista.append(nomes)
    print(nomes, lista.count(nomes))