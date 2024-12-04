import os 

f = open("input.txt", "r")
lines = f.readlines()

signs = {True: 1, False: -1}

def solve_line(level: list[int]) -> int:
    inc = level[1] > level[0]
    for i in range(1, len(level)):
        start, end = level[i - 1] + 1 * signs[inc], level[i - 1] + 3 * signs[inc]
        start, end = min(start, end), max(start, end)
        if level[i] < start or level[i] > end:
            return i
    return -1

def solve_2(level:list[int]) -> int:
    i = solve_line(level)
    if i == -1:
        return 1
    else:
        if i > 0:
            copy = level.copy()
            del copy[i - 1]
            if solve_line(copy) == -1:
                return 2
        if i < len(level) - 1:
            copy = level.copy()
            del copy[i + 1]
            if solve_line(copy) == -1:
                return 2
        copy = level.copy()
        del copy[i]
        if solve_line(copy) == -1:
            return 2
        
        copy = level.copy()
        del copy[0]
        if solve_line(copy) == -1:
            return 2
        
        copy = level.copy()
        del copy[-1]
        if solve_line(copy) == -1:
            return 2
    return 0

ans = {1:0, 2:0}
for line in lines:
    level = [int(v) for v in line.split()]
    i = solve_2(level)
    ans[1] += 1 if i == 1 else 0
    ans[2] += 1 if i != 0 else 0

print(f"1: {ans[1]}")
print(f"2: {ans[2]}")
