n = int(input())
r = 1
contador = 1
while True:
    if contador > n:
        break
    r *= contador
    contador += 1
print(r)