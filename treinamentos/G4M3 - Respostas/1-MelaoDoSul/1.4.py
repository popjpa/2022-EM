count = 0
lista = []
N = int(input())
for i in range(N):
    valores = int(input())
    lista.append(valores)
if lista[0] == 1:
    count += 1
for i in range(1, N):
    if lista[i-1] == 0 and lista[i] == 1:
        count += 1
print(count)