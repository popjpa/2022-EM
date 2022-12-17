string = 'Quanto tempo o tempo tem'
for i in string:
    if i.isalpha():
        print(f'{i} está no alfabeto! :D')
    else:
        print(f'{i} não está no alfabeto! D:')
        exit()