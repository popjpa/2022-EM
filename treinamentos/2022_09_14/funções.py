string = 'IFPB'

print(len(string))

print(string.find('a'))
print(string.find('P'))

print(string.replace('B', 'E'))
print(string.replace('I', 'U'))

string = 'POP é agro POP é tech POP é tudo'
print(string.split())

string = '       POP é agro POP é tech POP é tudo     '
print(string.strip())

string = '       POP é agro POP é tech POP é tudo     '
print(string.rstrip())
print(string.lstrip())

string = 'ifpb'
print(string.upper())

string = 'IFPB'
print(string.lower())

string = 'IFPB'
print(string.isalpha())
string = 'IFPB 12312312'
print(string.isalpha())

string = 'IFPB'
print(string.isdigit())
string = '12312312'
print(string.isdigit())

string = 'O sol está lindo hoje'
print(string.count('o'))
print(string.count('e'))
print(string.count(' '))


lista_string = ['Olá', 'tudo', 'bem?']
print(''.join(lista_string))

lista_string = ['8', '+', '8', '=', '16']
print(' '.join(lista_string))