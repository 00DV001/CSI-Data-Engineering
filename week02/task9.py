#task9, https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

set_len = int(input())
input_s = input().split()
li = []
for k in range(set_len):
    li.append(int(input_s[k]))
s = set(li) 
no_cmds = int(input())
sum = 0
for i in range(no_cmds):
    cmd = input().split()
    if 'pop' in cmd[0]:
        s.pop()
    elif 'remove' in cmd[0]:
        try:
            s.remove(int(cmd[1]))
        except:
            continue
    elif 'discard' in cmd[0]:
        try:
            s.discard(int(cmd[1]))
        except:
            continue
for j in range(len(s)):
    l2 = list(s)
    sum += l2[j]
print(sum)