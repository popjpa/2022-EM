P = int(input())
soma_meloes = 0
soma_goblins = 0
while True:
    F, M, G = map(int, input().split())
    if F == 0 and M == 0 and G == 0:
        break
    elif P < F:
        soma_meloes += M
        soma_goblins += G
        print(f'Meloes roubados: {soma_meloes}')
        print(f'Goblins resgatados: {soma_goblins}')
        print('---')
    else:
        print(f'Meloes roubados: {soma_meloes}')
        print(f'Goblins resgatados: {soma_goblins}')
        print('---')