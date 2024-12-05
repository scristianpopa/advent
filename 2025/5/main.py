import os


f = open("input.txt", "r")
lines = f.readlines()
n = len(lines)
for i in range(n):
    lines[i] = lines[i].strip()
inp = True

ans = {1: 0, 2: 0}
before = {i: set() for i in range(100)}


def solve1(l: list[int]) -> int:
    n = len(l)
    for i in range(n):
        presence = [v in before[l[i]] for v in l[i + 1: n]]

        if any(presence):
            return 0
    return l[n // 2]


def solve2(l: list[int]):
    n = len(l)
    i = 0
    changed = False
    while i < n:
        presence = [v in before[l[i]] for v in l[i + 1: n]]
        shift = 1
        while any(presence) and i + shift < n:
            changed = True
            l[i + shift - 1], l[i + shift] = l[i + shift], l[i + shift - 1]
            shift += 1
            presence = [v in before[l[i]] for v in l[i + 1: n]]
        if shift == 1:
            i += 1
    return l[n // 2] if changed else 0


for i in range(n):
    if lines[i] == '':
        inp = False
        continue

    if inp:
        x, y = [int(v) for v in lines[i].split('|')]
        before[y].add(x)
    else:
        l = [int(v) for v in lines[i].split(',')]
        ans[1] += solve1(l)
        ans[2] += solve2(l)

print(f"1: {ans[1]}")
print(f"2: {ans[2]}")
