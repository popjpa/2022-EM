t = int(input())
for i in range(t):
    n = int(input())
    valores = list(map(int, input().split()))
    valores2 = []
    maior1 = max(valores)
    menor1 = min(valores)
    sub1 = maior1 - menor1
    cont1 = cont2 = 0
    for j in range(len(valores)):
        if valores[j] == maior1:
            if cont1 == 0:
                cont1 += 1
            else:
                valores2.append(valores[j])
        elif valores[j] == menor1:
            if cont2 == 0:
                cont2 += 1
            else:
                valores2.append(valores[j])
        else:
            valores2.append(valores[j])
    maior2 = max(valores2)
    menor2 = min(valores2)
    sub2 = maior2 - menor2
    print(sub1 + sub2)