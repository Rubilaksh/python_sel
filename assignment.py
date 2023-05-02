# marks = [90,58,67,89,99]

def calculate_average():
    marks = [90, 58, 67, 89, 99]
    sum_of_marks = 0
    for i in marks:
        sum_of_marks = sum_of_marks + i

    average = sum_of_marks / len(marks)
    return average


def calculate_grade(average):
    if result >= 80:
        print("The average is {} and the grade is A".format(result))
    elif result >= 60:
        print("The average is {} and the grade is B".format(result))
    elif result >= 50:
        print("The average is {} and the grade is C".format(result))
    else:
        print("The average is {} and the grade is F".format(result))


result = calculate_average()
print(result)

calculate_grade(result)
