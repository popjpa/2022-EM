n = int(input())
l = list(map(int, input().split()))
l.sort()
r = l[1] - l[0]
pa = False
for i in range(n- 1):
    if i < n - 1:
        if l[i+1] - l[i] == r:
            pa = True
        else:
            pa = False
            break
    else:
        if l[n - 1] - l[n-2] == r:
            pa = True
        else:
            pa = False
if pa == True:
    print('TRUE')
else:
    print('FALSE')