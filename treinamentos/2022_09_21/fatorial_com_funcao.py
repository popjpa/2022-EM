def fatorial(valor):
    if valor == 0 or valor == 1:
        return 1
    return valor * fatorial(valor-1)

valor = int(input())
print(fatorial(valor))