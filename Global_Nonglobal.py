# Function to showcase global and non-global variables
message="how are you"

def multiplication(first_num, second_num):
    result = first_num * second_num
    return result

def greet():

    message1= "Am fine"
    global message

    print ("Inside function--> ", message1)


# print(result)

#output=multiplication(10, 25)
#print(output)

greet()
print("Outside function-->", message)