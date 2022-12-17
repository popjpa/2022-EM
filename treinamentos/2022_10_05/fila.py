from collections import deque

fila = deque()
for i in range(10):
    fila.append(i+1)
print(fila[5])