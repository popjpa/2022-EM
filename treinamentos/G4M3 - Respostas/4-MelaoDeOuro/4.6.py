slimes = list(map(int, input().split()))
N = len(slimes)
count = 0
while slimes != [1] * N:
    for i in range(N):
        if slimes[i] != 1 and slimes[i] % 2 != 0:
            slimes[i] += 1
        elif slimes[i] % 2 == 0:
            slimes[i] //= 2
    count += 1
print(count)