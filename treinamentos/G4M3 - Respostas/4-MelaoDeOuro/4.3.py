N = int(input())
print(N)
while N != 1:
    if N % 2 != 0:
        N = 3 * N + 1
        N = int(N)
        print(N)
    else:
        N /= 2
        N = int(N)
        print(N)