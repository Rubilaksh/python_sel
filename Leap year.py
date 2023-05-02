year = int(input("Enter the the year:"))
if (year % 100 == 0) and (year % 400 == 0):
    print("{} is a Leap year".format(year))
elif(year % 4 ==0) and (year % 100 != 0):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))