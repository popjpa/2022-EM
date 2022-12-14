H, C, S, P, W = input().split()
H, C, S, P, W = int(H), int(C), int(S), int(P), float(W)
quali_peso = []
for i in range(4):
    qualidade = input()
    peso = input()
    quali_peso.append([float(qualidade), float(peso)])
quali_peso.sort(reverse=True)
c = 0
q = 0
for i in range(len(quali_peso)):
    if c <= float(W):
        c += float(quali_peso[i][1])
        q += float(quali_peso[i][0])
print(q)