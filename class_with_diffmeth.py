class list_programs:

    def armstrong(self,b):
        self.num = b
        summ = 0
        length = len(str(self.num))
        for i in str(self.num):
            res = int(i) ** length
            summ += res

        if summ == self.num:
            print("Armstrong number")
        else:
            print("not armstrong number")


    def celsious_to_faren(self,b):
        self.temp = b
        value = (self.temp * 1.8) + 32
        return value


    def factorial(self, b):
        self.num = b
        fact = 1
        if b < 0:
            print("invalid number")
        elif b == 0:
            print("Enter value other than 0")
        else:
            for i in range(self.num+1):
                fact = fact * i
                return fact




a1 = list_programs()
a1.armstrong(10)

a2 = list_programs()
result = a2.celsious_to_faren(36)
print(result)

a3 = list_programs()
result = a3.factorial(10)
print(result)