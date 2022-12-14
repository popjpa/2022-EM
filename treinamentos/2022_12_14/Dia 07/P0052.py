n = int(input())
string = input()
cont = 0
i = inicio = 0
resultado = []
entrar = True
while i < n:
    inicio = i
    entrar = True
    distintas = [string[i]]
    for j in range(inicio, len(string)):
        if string[j] not in distintas and entrar == True:
            distintas.append(string[j])
            entrar = False
            cont += 1
        elif string[j] in distintas:
            cont += 1
        else:
            break
    i += 1
    resultado.append(cont)
    cont = 0
    distintas.clear()
print(max(resultado))