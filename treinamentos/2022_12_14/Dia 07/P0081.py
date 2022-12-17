n = int(input())
l = []
c = 100
for i in range(n):
  l.append(int(input()))
for i in range(n):
  if sum(l[0:i]) - sum(l[i:n]) > 0:
    if sum(l[0:i]) - sum(l[i:n]) < c:
      c = sum(l[0:i]) - sum(l[i:n])
  else:
    if sum(l[i:n]) - sum(l[0:i]) < c:
      c = sum(l[i:n]) - sum(l[0:i])
print(c)