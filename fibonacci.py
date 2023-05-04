#Program to find the fibonacci series
"""
def fib(n):
    #n = int(input("Enter the value of n: "))
    a = 0
    b = 1
    if n < 0:
        print("Invalid number")
    elif n == 0:
        print(n)
    elif n == 1:
        print(n)
    elif n > 1:
        for i in range(1, n):
            c = a+b
            a = b
            b = c
        print(b)


print(fib(3))
"""

n = int(input("Enter the value of n:"))
a = 0
b = 1
count = 0
if n < 0:
    print("Invalid number")
elif n == 0:
    print(n)
else:
    while count < n:
        print(a)
        c = a+b
        a = b
        b = c
        count += 1


