'''
num = int(input("Enter the number:"))
summ = 0

length = len(str(num))
for i in str(num):
    res = int(i) ** length
    summ += res
    print(summ)
if summ == num:
    print("Armstrong number")
else:
    print("not armstrong number")

'''

num = int(input("enter the number:"))
summ = 0
length = len(str(num))
for i in str(num):
    res = int(i) ** length
    summ += res

if summ == num :
    print("Armstrong number")
else:
    print("not armstrong number")