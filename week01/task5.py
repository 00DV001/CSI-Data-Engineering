#task5, https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
from itertools import combinations as comb
N = int(input())
input_str = input()
L1 = list(input_str.replace(" ", ""))[:N]

r = int(input()) #selected no of indices
selected_char = 'a'

all_combs = list(comb(L1,r))
total_combs = len(all_combs)

fav_combs = 0
for c in all_combs:
    if selected_char in c:
        fav_combs +=1

if total_combs > 0:
    probability = fav_combs/total_combs
    print(f"{probability:.3f}")
else:
    print("No combinations possible")