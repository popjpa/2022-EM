n, m = map(int, input().split())
numEstrelas = []
valorNutritivo = []
valorNutritivo2 = []
for i in range(n):
    q, v = map(int, input().split())
    numEstrelas.append(q)
    valorNutritivo.append(v)
for i in range(n):
    if numEstrelas[i] > 1:
        while numEstrelas[i] != 0:
            valorNutritivo2.append(valorNutritivo[i])
            numEstrelas[i] -= 1
    else:
        valorNutritivo2.append(valorNutritivo[i])
valorNutritivo2.sort(reverse=True)
numEstrelas2 = [1] * len(valorNutritivo2)
numEstrelas2.sort(reverse=True)
i = 0
cont = 0
while m > 0:
    cont += valorNutritivo2[i]
    m -= 1
    i += 1
print(cont)
