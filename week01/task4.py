#task4, https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    leap = False
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))