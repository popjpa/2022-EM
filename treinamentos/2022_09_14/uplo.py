a = input()
cont_mai = cont_min = 0
for i in a:
    if i == i.upper():
        cont_mai += 1
    elif i == i.lower():
        cont_min += 1
if cont_mai > cont_min:
    print(a.upper())
else:
    print(a.lower())