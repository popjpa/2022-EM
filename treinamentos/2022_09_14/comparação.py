string = 'o dia esta lindo'
for i in string:
    if i >= 'A' and i <= 'Z':
        print(f'{i} é uma letra maiuscula')
    elif i >= 'a' and i <= 'z':
        print(f'{i} é uma letra minuscula')
    elif i.isdigit():
        print(f'{i} é um número :O')
    else:
        print(f'{i} é um caracter especial')