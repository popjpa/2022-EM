N, E = map(int, input().split())
soma = 0
for i in range(N):
    soma += int(input())
if soma >= E:
    print("NADA PREOCUPANTE")
elif soma >= E - 5:
    print("POUCO PREOCUPANTE")
else:
    print("MUITO PREOCUPANTE")