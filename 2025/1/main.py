import os 

f = open("input.txt", "r")
lines = f.readlines()

l,r = [], []
for line in lines:
    x, y = [int(v) for v in line.split()]
    l.append(x)
    r.append(y)

l = sorted(l)
r = sorted(r)

ans = 0
for i in range(len(l)):
    ans += abs(l[i] - r[i])
print(f"1: {ans}")

rm = {}
for v in r:
    if v not in rm:
        rm[v] = 1
    else:
        rm[v]+=1

ans = 0
for v in l:
    ans += v * rm.get(v, 0)
print(f"2: {ans}")