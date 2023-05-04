#function to add 2 nos
def add_two_nos(firstNo, secondNo):
    result = firstNo+secondNo
    print("Addition of 2 nos is ",result)
    print("Addition of 2 nos using format {}".format(result))

def add_two_nos_return(firstNo, secondNo):
    result= firstNo+secondNo
    return result

#function call
add_two_nos(15.7,25.3)

additionValue= add_two_nos_return(10,15)

#Printing the value
print("Addition of 2 nos is ",additionValue)
