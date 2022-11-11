P = input()
retirar = 'P'
for i in range(len(retirar)):
    if 'PPP' not in P:
        P = P.replace(retirar[i], '')
    else:
        P = P.replace('PPP', '--')
        P = P.replace(retirar[i], '')
P = P.replace('--', 'P')
print(P)