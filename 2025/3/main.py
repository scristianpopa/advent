import os 
import re

f = open("input.txt", "r")
lines = f.readlines()

ans = 0

for line in lines:
    matches = re.findall("mul\(\d+,\d+\)", line)
    for m in matches:
        numbers = re.findall("\d+", m)
        ans += int(numbers[0]) * int(numbers[1])

print(f"1: {ans}")

en = True

ans = 0

for line in lines:
    matches = re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", line)
    for m in matches:
        if m == "do()":
            en = True
        elif m == "don't()":
            en = False
        else:
            numbers = re.findall("\d+", m)
            if en:
                ans += int(numbers[0]) * int(numbers[1])

print(f"2: {ans}")
