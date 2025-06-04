#task2, https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
import itertools
str = input()
keys = []
groups = []
for k, g in itertools.groupby(str):
    keys.append(k[0])
    groups.append(list(g))

for j in range(len(groups)):
    print(f"({len(groups[j])}, {keys[j]})", end =" ")