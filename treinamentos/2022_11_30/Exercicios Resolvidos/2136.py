lista_inscritos = []
lista_negativos = []
lista_incristos_nao_ordenada = []
qntd_letras_amigo = 0
while True:
    nomes = input().split()
    if nomes[0] == 'FIM':
        break
    if (nomes[1] == 'YES') and (nomes[0] not in lista_inscritos):
        qntd_letras = len(nomes[0])
        if qntd_letras > qntd_letras_amigo:
            amigo_habay = nomes[0]
            qntd_letras_amigo = qntd_letras
        lista_inscritos.append(nomes[0])
        lista_incristos_nao_ordenada.append(nomes[0])
    elif (nomes[1] == 'NO'):
        lista_negativos.append(nomes[0])
lista_inscritos.sort()
lista_negativos.sort()
lista_total = lista_inscritos + lista_negativos
for i in lista_total:
    print(i)
print()
print(f'Amigo do Habay:\n{amigo_habay}')