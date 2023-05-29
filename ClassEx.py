class student:

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def check_pass_fail(self):
        if self.marks >= 40:8
          #  status="passed"
           # return status
            return "pass"

        else:
            return "fail"

s1 = student("arun",90)
result= s1.check_pass_fail()
print("Te result of ",s1.name," is ",result)

s2= student("nirmal",30)
result1= s2.check_pass_fail()
print("Te result of ",s2.name," is ",result1)
