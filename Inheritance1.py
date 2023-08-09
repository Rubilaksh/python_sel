class Arithmetic:

    '''

    1. declare a global variable and assign some integer value
    2. create a method (summation) to add 2 values + global variable value

    '''
    value_of_c = 10

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def summation(self):
        summ = self.a + self.b + self.value_of_c
        return summ

s1 = Arithmetic(20,30)
result = s1.summation()
print(result)