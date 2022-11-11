N, R = map(int, input().split())
valores = list(map(int, input().split()))
for i in valores:
    if i <= R:
        print(1)
    else:
        print(0)