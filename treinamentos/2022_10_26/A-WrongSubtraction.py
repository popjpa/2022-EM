x, y = map(int, input().split())
while y != 0:
    if int(str(int(x/1))[-1]) == 0:
        x /= 10
    else:
        x -= 1
    y -= 1
print(int(x))