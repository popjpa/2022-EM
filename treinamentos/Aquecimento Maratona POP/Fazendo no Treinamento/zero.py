a = float(input())
x = a // 30
y = (a % 30) * 2
x, y = int(x), int(y)
print("{}h{}m".format(x, y))