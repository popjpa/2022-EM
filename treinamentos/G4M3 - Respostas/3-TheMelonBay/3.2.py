N = int(input())
valores = list(map(int, input().split()))
zero = len(valores) // 2
count = 0
for i in range(zero):
    valores[i] += valores[i+1]
    valores[i] = 0
    count += 1
for i in range(len(valores)-1, zero, -1):
    valores[i] += valores[i-1]
    valores[i] = 0
    count += 1
print(count)