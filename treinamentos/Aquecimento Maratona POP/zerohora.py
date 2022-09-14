x = float(input())
x = x * 2
hora = x // 60
hora = int(hora)
x -= (hora * 60)
x = int(x)
print(f"{hora}h{x}m")