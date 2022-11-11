def get_esconderijo(line, pos):
    if pos < 0:
        return 'X'
    if pos >= len(line):
        return 'X'
    return line[pos]

pos = 0
count = 0
while True:
    line = input()
    if 'X' not in line:
        break
    if get_esconderijo(line, pos) == 'X':
        print('Silêncio...')
    elif get_esconderijo(line, pos) == 'O' and get_esconderijo(line, pos + 1) == 'X' and get_esconderijo(line, pos - 1) == 'X':
        print('Tiro de Melão!!!')
        count += 1
    elif get_esconderijo(line, pos) == 'O' and get_esconderijo(line, pos + 1) == 'O' and get_esconderijo(line, pos - 1) == 'X':
        pos += 1
        print(f'Correndo pro esconderijo {pos}!')
    elif get_esconderijo(line, pos) == 'O' and get_esconderijo(line, pos - 1) == 'O' and get_esconderijo(line, pos + 1) == 'X':
        pos -= 1
        print(f'Correndo pro esconderijo {pos}!')
    elif get_esconderijo(line, pos) == 'O' and get_esconderijo(line, pos - 1) == 'O' and get_esconderijo(line, pos + 1) == 'O':
        print('Tiro de Melão!!!')
        count += 1
print(f'Vitória com {count} melões!')