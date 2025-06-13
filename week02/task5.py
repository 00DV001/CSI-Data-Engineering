#task5, https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    # your code goes here
    l1=[]
    i = 0
    kvalue = k
    j = 0
    while i < len(string):
        l1.append(string[i:kvalue])
        i = i+k
        kvalue = kvalue+k
    for x in range(len(l1)):
        print(''.join(set(l1[x])))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)