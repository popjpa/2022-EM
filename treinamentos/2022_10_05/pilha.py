from collections import deque
pilha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pilha.pop()
pilha.append(100)
'''for i in range(len(pilha)-1, -1, -1):
    print(pilha[i])'''


pilha2 = deque()
for i in range(10):
    pilha2.append(i+1)
a = pilha2.pop()
print(pilha2)
print(a)


'''for i in pilha[::-1]:
    print(i)'''