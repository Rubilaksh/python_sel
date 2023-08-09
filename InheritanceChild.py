from Inheritance1 import Arithmetic


class ChildImp(Arithmetic):
    num2=10

    def __init__(self):
        Arithmetic.__init__(self, 20,30)

    def get_complete_data(self):
        data = self.num2+ self.summation()
        return data

obj1= ChildImp()
result=obj1.get_complete_data()
print("The resultant value is ", result)



