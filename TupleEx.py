values1= ("learning", 2.5, "python", 1, 2.5, "learning")

#Tuple is immutable --> which means that we cant add or delete elements to a tuple
print(values1[1])

print(values1[-1])
print(values1[0:2])

#values1[2]="new value"
#print(values1)

#counts the no. of occurences of the given value
print(values1.count(2.5))
print(values1.count("python"))

#index--> returns the first occurence of the given value
print(values1.index("learning"))
print(values1.index(1))

print(values1.index("learning", 1))

print(values1.index(2.5, 2, 5))
