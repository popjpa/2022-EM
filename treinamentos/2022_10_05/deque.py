from collections import deque

fila = deque()
for i in range(10):
    fila.append(i+1)
fila.popleft()
fila.remove(5)
fila.append(100)
print(fila)