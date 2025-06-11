#task1, https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
import string
def solve(s):
    print(string.capwords(s,sep= ' '))
str1 = input()
result = solve(str1)