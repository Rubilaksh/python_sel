class School:
    school_name = ""

    def student(self):
        print("Student of",self.school_name)

class Student_info(School):

    def student_name(self):
        print("student name is Jai")

s1 = Student_info()
s1.school_name = "Zion"
s1.student()
s1.student_name()