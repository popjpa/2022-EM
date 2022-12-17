from collections import deque

n = int(input())
for i in range(n):
    cont = 0
    pilha = deque()
    s = input()
    for i in s:
        if i == '<':
            pilha.append(i)
        elif i == '>' and len(pilha) > 0:
            cont += 1
            pilha.pop()
    print(cont)