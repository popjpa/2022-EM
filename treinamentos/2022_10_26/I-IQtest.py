n = int(input())
valores = list(map(int, input().split()))
pares = impares = 0
for i in valores:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
if pares > impares:
    for i in range(n):
        if valores[i] % 2 != 0:
            print(i+1)
            break
else:
    for i in range(n):
        if valores[i] % 2 == 0:
            print(i+1)
            break