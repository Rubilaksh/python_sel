values = {1, 2, 3, 1, 5}
listValues = [1, 2, 3, 1]
myset = set(["a",1, "b", 10.2, "a"])

# Set doesn't maintain order and doesn't allow duplicates. Set is heterogenous
print("Set Values-->",values)
print("List Values-->",listValues)
print("using set method-->",myset)

'''
#We cant change value in a set because its immutable
values[1]="learning"
print("Set after changing the value-->",values)

'''

#Adding a value to a set
myset.add(25)
print("Printing set after adding value-->", myset)

#Removing an elemt from a set
myset.remove(25)
print("Printing set after removing the value-->", myset)

print("Hello I am learning {} and {}". format("python", "selenium"))

#Union of sets --> merging of 2 sets
set1={1,2, 3, 4, 5}
set2 ={3,4,5,6,7,8,9}

set3 = set1.union(set2)
print(set3)

#Intersection of sets--> common elements in sets
set4 = set1.intersection(set2)
print(set4)

#Difference of sets
set5 = set1.difference(set2)
print(set5)

set6 = set2-set1
print(set6)
