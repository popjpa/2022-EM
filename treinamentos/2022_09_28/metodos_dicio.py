dicionario = {}
a = 'a'
for i in range(5):
    dicionario[i+1] = a
    a += 'a'

dicionario.clear()

for i in range(5):
    dicionario[i+1] = a
    a += 'a'

dicionario.update(Jacyel = 20)
dicionario['Jacyel'] = 30
dicionario.update(Jacyel = 20)

dicionario_segundo = dicionario.copy()

dicionario.pop(3)

print(dicionario)
print(dicionario_segundo)