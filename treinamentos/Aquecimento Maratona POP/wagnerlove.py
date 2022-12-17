from string import ascii_lowercase
n = int(input())
s = input()
a = s.lower()
numeros = ['0', '1', '2', '3', '4' , '5', '6', '7', '8', '9']
for i in a:
    if i in numeros:
        print(s + ' YES')
        exit()
print(s + ' NO')