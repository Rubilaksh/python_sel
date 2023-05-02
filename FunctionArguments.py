def multiplication(first_num= 10, second_num=30):
    print("first number ", first_num)
    print("second number ", second_num)
    result = first_num * second_num
    print(result)

#Positional arguments --> assigns values based on the positional index to the function definition
multiplication(10, 20)

#default functional arguments
multiplication(10)
multiplication()

#keyword arguments
multiplication(second_num=25, first_num=20)
