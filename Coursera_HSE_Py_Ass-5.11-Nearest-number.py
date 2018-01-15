
l = int(input())
a = list(map(int, input().split()))
n = int(input())
na = []

for i in a:
    t = n - i
    if t >= 0:
        na.append(t)
    else:
        na.append(t * (-1))

ta = na[0]
for i in range(0, len(na)):
    if ta >= na[i]:
        ta, ti = na[i], i

print(a[ti])
