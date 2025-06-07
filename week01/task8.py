def print_formatted(number):
    if number < 1 or number > 99:
        print("constraint error")
    else:
        width = len(bin(number)) - 2
    
    for i in range(1,number+1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)