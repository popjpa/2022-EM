n, k = map(int, input().split())
aux = 0
if n % 2 == 0:
    aux = n // 2
else:
    aux = (n + 1) // 2;
    
if k <= aux:
    print(k * 2 - 1)
else:
    print((k - aux) * 2)