from string import ascii_lowercase
n = int(input())
s = input()
a = s.lower()
alfa = ascii_lowercase
for i in a:
    if i not in alfa:
        print(s + ' YES')
        exit()
print(s + ' NO')