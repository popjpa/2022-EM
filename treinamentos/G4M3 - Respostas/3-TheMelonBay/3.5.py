N = int(input())
lista = []
maiores = []
while len(lista) != N:
    valores = int(input())
    if valores != 0:
        lista.append(valores)
    else:
        maiores.append(max(lista))
        lista.remove(max(lista))
for s in maiores:
    print(s)