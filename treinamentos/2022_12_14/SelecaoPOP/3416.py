N, L, D = map(int, input().split())
aux = L
conta = N * D / 1000 
if conta < L or conta == L:
    print(L)
else:
    while L < conta:
        L += aux
    print(L)