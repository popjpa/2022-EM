t = int(input())
cont = 0
for i in range(t):
    n = int(input())
    string = input()
    new_string = ''
    for j in range(n):
        if len(new_string) == 0 and string[j] == 'y':
            new_string += string[j]
        elif len(new_string) == 1 and string[j] == 'e':
            new_string += string[j]
        elif len(new_string) == 2 and string[j] == 's':
            new_string += string[j]
            cont += 1
            new_string = ''
    print(cont)
    new_string = ''
    cont = 0