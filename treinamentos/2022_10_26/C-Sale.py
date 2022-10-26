n, m = map(int, input().split())
v = list(map(int, input().split()))
negativos = [i for i in v if i < 0]
negativos.sort()
print(-sum(negativos[:m]))