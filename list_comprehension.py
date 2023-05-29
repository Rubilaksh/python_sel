"""
fruits = ["orange", "apple", "grapes", "plum"]
fruits_with_a = []
for i in fruits:
    if "a" in i:
        fruits_with_a.append(i)

print(fruits_with_a)
"""

fruits = ["orange", "apple", "grapes", "plum"]
"""
fruits_with_a = [i for i in fruits if "a" in i]
print(fruits_with_a)
"""
fruits_not_apple = [i.upper() for i in fruits if i != "apple"]
print(fruits_not_apple)
print(type(fruits_not_apple))
fruits_not_apple.insert(-1,"mango")
print(fruits_not_apple)
fruits_not_apple.append("mango")
print(fruits_not_apple)
fruits_not_apple.insert(2,"strawberry")
print(fruits_not_apple)
fruits_not_apple.remove("mango")
print(fruits_not_apple)
list2 = [1,2,3,43]
fruits.extend(list2)
print(*fruits, sep = "\n")
