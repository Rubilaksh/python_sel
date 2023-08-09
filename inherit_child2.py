from Inheritance1 import Arithmetic
from InheritanceChild import ChildImp

class Multiplication(Arithmetic):
    c = 10

    def __init__(self):
        Arithmetic.__init__(self,30,40)

    def product(self):
        prod = self.summation() * self.c
        return prod

m1 = Multiplication()
result = m1.product()
print(result)

class Calc(ChildImp):
    gvar = 20
    def __init__(self):
        ChildImp.__init__(self)

    def addition(self):
        summ = self.get_complete_data() + self.gvar
        return summ

a1 = Calc()
result = a1.addition()
print(result)



