import re

n = int(input())

matches = []

for _ in range(n):
    line = input()
    x = re.split("^Simon says ", line)
    if len(x) > 1:
        matches.append(x[1])

for match in matches:
    print(match)