#task2, https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
def average(array):
# your code goes here
    sumSet = set(array)
    sumf = 0
    for i in sumSet:
        sumf = sumf + i
    
    finalaverage = sumf/len(sumSet)
    return finalaverage

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)