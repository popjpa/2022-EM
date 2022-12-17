n = int(input())
dict = {}
for i in range(n):
    s = input()
    if s not in dict:
        dict[s] = 0
        print("OK")
    else:
        dict[s] += 1
        print(s + str(dict[s]))