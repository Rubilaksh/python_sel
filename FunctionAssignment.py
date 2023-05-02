#marks[90,58,67,89,99]
#calculate the average of these marks (calculate_average). If the average is grater than 80 (Grade A)
# 60 --> Grade B, 50-->Grace C, less than 50 --> grade F (calculate_grade)
marks = [90,58,67,89,99]

def calculate_average():
    res = sum(marks)/len(marks)
    return res


result = calculate_average()
print(result)
if result >= 80:
    print("The average is {} and the grade is A".format(result))
elif result >= 60:
    print("The average is {} and the grade is B".format(result))
elif result >= 50:
    print("The average is {} and the grade is C".format(result))
else:
    print("The average is {} and the grade is F".format(result))