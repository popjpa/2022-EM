n = int(input())
for i in range(n):
    minutos, tempo = input().split()
    minutos = int(minutos)
    if tempo == '1T':
        if minutos <= 45:
            print(minutos)
        else:
            print(f'45+{minutos-45}')
    else:
        if minutos <= 45:
            print(45 + minutos)
        else:
            print(f'90+{minutos-45}')