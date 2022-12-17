pes = int(input())
meloes = int(input())
producao_esperada = int(input())

producao_real = pes * producao_esperada

if meloes < producao_real:
    print('SIM')
else:
    print('NAO')