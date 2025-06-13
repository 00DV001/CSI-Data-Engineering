#task4, https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
import string
def print_rangoli(size):
    # your code goes here
    size = size -1
    abc = string.ascii_lowercase
    if size < 0 or size >= len(abc):
        print("Invalid size. Enter a number between 0 and 25.")
        return
    half = list(abc[size::-1])
    full = half + half[-2::-1]
    width = len('-'.join(full))
    lines = []
    for i in range(size):
        left = half[:i+1]
        right = left[:-1][::-1]
        line = '-'.join(left + right)
        lines.append(line.center(width, '-'))
    lines.append('-'.join(full))
    lines += lines[-2::-1]
    for line in lines:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)