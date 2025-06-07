#task6, https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
#Note: hash function gives different output for different python versions
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list = list(integer_list)
    t = tuple(integer_list)
    print(hash(t))