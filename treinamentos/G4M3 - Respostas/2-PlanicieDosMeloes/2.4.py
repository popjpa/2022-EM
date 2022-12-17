beleza1 = 0
beleza2 = 0
v1 = input()
v2 = input()
v3 = input()
v4 = input()
ultima1 = v1.split()[-1]
ultima2 = v2.split()[-1]
ultima3 = v3.split()[-1]
ultima4 = v4.split()[-1]
for i in range(len(ultima1)):
    ultimos_1 = ultima1[-i:]
    ultimos_2 = ultima2[-i:]
    ultimos_3 = ultima3[-i:]
    ultimos_4 = ultima4[-i:]
    if ultimos_1 == ultimos_3:
        beleza1 += 1
    if ultimos_2 == ultimos_4:
        beleza2 += 1
print(beleza1 + beleza2)