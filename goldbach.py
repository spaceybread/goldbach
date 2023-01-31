m = []

p = [2, ]
n = 2

while len(p) <= 10:
    i = 0
    while (n % p[i]) != 0:
        if len(p) != (i + 1):
            i = i + 1
        else:
            p.append(n)
            break
    n = n + 1


i = 4
while i < p[len(p) - 1]:
    m.append(i)
    i = i + 2

i = 0
while i < len(m):
    add = []
    n = 0
    add.append(m[i])
    while (n < len(p) and p[n] < m[i]):
        if (m[i] - p[n]) in p:
            add.append([m[i] - p[n], p[n]])
        n = n + 1
    i = i + 1

    print(add)
