
#Funtions is a block of code which performs a specific task.
# Moreover this functions can be reused whereas possible

#we should first define the function and then only call by its name
def greet():
    print("Hello")
    print("How are you")

def greet_with_name(firstname):
    print("Hello {} ".format(firstname))
    print("How are you {}".format(firstname))

#Function call
greet()

greet_with_name("Jack")
