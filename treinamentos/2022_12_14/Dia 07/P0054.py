n = int(input())
l = list(map(int, input().split()))
menor = l.index(min(l))
menor_valor = min(l)
lucros = []
for i in range(menor+1, n):
    lucros.append(abs(menor_valor - l[i]))
print(max(lucros))