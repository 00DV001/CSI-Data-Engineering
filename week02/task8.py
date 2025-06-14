#task8, https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
#Python 2
import re
T = int(input())
for i in range(T):
    S = input()
    try :
        if re.compile(S.strip()) != None:
            print('True')
    except:
        print('False')