from collections import deque
while True:
    try:
        s = input()
        pilha = deque()
        r = True
        for i in s:
            if i == '(':
                pilha.append(i)
            elif i == ')':
                if len(pilha) == 0:
                    r = False
                    break
                else:
                    pilha.pop()
        if len(pilha) == 0 and r == True:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break