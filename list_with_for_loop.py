"""
list1 = [1,2,3,4,5]

for i in range(len(list1)+1):
    print(i)

    """

list1 = [1,2,3,4,5]

print(*list1)

print(*list1, sep = " , ")

print(*list1, sep = "\n")

a = ["my","name", "is", "Rubini"]
print(" " .join(a))

a1 = [1,2,3,4,5]
print(str(a1)[1:-1])