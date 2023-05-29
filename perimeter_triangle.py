class triangle:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c



    def perimeter(self):
        summ = self.a + self.b + self.c
        return summ

p1 = triangle(2,3,4)
result = p1.perimeter()
print(result)

p2 = triangle(10,20,30)
res = p2.perimeter()
print(res)



