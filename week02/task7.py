#task7, https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
T = int(input())
for i in range(T):
    try:
        input_values = input().split()
        a = int(input_values[0])
        b = int(input_values[1])
        try:
            print(a//b)
        except ZeroDivisionError as e:
            e = 'integer division or modulo by zero'
            print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)