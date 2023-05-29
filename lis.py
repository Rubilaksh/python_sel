list1=["python", "java", 10]
list1.append("a")
list1.append(5)

print(list1)


class employee:

    def __init__(self,name):
        self.name = name


    def emp(self):
        emp_details = (self.name)
        return emp_details

e1 = employee(["john", 30])
result = e1.emp()
print(result)

