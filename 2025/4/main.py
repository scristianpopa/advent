import os
import re

f = open("input.txt", "r")
lines = f.readlines()

n = len(lines)
for i in range(n):
    lines[i] = lines[i].strip()

prim_diag = []
for i in range(-n + 1, n):
    d = ""
    for j in range(max(0, -i), min(n - i, n)):
        d += lines[i + j][j]
    prim_diag.append(d)

sec_diag = []
for i in range(2 * n - 1):
    d = ""
    for j in range(max(0, i - n + 1), min(i + 1, n)):
        d += lines[j][i - j]
    sec_diag.append(d)

transp = []
for i in range(n):
    transp.append("".join([lines[j][i] for j in range(n)]))

ans = 0
for line in lines + transp + sec_diag + prim_diag:
    matches = re.findall("XMAS", line)
    ans += len(matches)
    matches = re.findall("SAMX", line)
    ans += len(matches)

print(f"1: {ans}")


ans = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if (lines[i][j] == 'A' and
            ((lines[i-1][j-1] == 'S' and lines[i + 1][j + 1] == 'M') or (lines[i-1][j-1] == 'M' and lines[i + 1][j + 1] == 'S')) and
                ((lines[i+1][j-1] == 'S' and lines[i - 1][j + 1] == 'M') or (lines[i+1][j-1] == 'M' and lines[i - 1][j + 1] == 'S'))):
            ans += 1

print(f"2: {ans}")
