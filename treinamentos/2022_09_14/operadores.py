a = 'Zé'
b = 'Zé'
print(id(b))
c = 'Shingeki'
d = 'Ruim'

if a == b: #a is b
    print('Strings Iguais :)')
else:
    print('Strings Diferentes :(')
print()
if c != d: #a != b
    print(f"{c} não é {d}")
else:
    print(f'{c} é {d}')
