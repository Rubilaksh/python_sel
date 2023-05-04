#program to find factorial of nos
num = int(input("Enter the number:"))
factorial = 1
if num < 0:
    print("{} is invalid number".format(num))
elif num == 0:
    print("factorial of {} is 1".format(num))
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("Factorial of", num, "is {}".format(factorial))
