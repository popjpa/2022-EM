x = float(input())
x = x * 2
hora = x // 60
hora = int(hora)
x = x - (hora * 60)
x = int(x)
print("{}h{}m".format(hora,x))