n = int(input())
cont = 0
for i in range(n):
    p, v, t = map(int, input().split())
    if (p + v + t > 1):
        cont += 1
print(cont)