dict1 = {1: "red", "learn": "python", "red": 3, 4: {"name": "test", 5: "red"} }
dict2 = dict({1: "red", 2: "black", 3: "green"})
dict3 = dict([(1, "yellow"), (2, "red")])

print(dict1)
print(dict2)
print(dict3)

print(dict1[1])
print(dict1["learn"])
print(dict1[4])
print(dict1[4]["name"])
print(dict1[4][5])

print(dict2.get(2))

dict1["new"]="new value"
dict1[7]="yellow"
print(dict1)

dict1["learn"]= "java"
print(dict1)

#inbuilt methods in dictionary
'''
copy
clear
get
items
pop
popitem
keys
values
update

'''

dict4= dict1.copy()
print (dict4)

print(dict4.clear())

print(dict1.get(4).get("name"))

print("Items",dict2.items())

print(dict2.keys())

print(dict2.values())

dict2.pop(3)
print(dict2)

dict2.popitem()
print(

)

dict2.update({1:"blue"})
print(dict2)






