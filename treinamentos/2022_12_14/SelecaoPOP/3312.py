n = int(input())
l = list(map(int, input().split()))
for i in l:
    c = 0
    f = 1
    if i > 1:
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
        if c == 2:
            for j in range(i, 0, -1):
                f *= j
            print(f'{i}! = {f}')