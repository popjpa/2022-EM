T, N = map(int, input().split())
for i in range(T):
    cidades_acessiveis = []
    cont = 0
    cidades = list(map(int, input().split()))
    for j in range(1, N):
        conta = cidades[0] - cidades[j]
        if conta <= 2 and conta >= 0:
            cont += 1
            cidades_acessiveis.append(cidades[j])
            cidades[j] = -100
    tamanho = len(cidades_acessiveis)
    j = 0
    while tamanho > 0:
        for k in range(1, N):
            conta = cidades_acessiveis[j] - cidades[k]
            if conta <= 2 and conta >= 0:
                cont += 1
                cidades_acessiveis.append(cidades[k])
                tamanho += 1
                cidades[k] = -100
        tamanho -= 1
        j += 1
    print(cont)     