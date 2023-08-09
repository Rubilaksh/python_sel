itemsInCart=0

'''
#First way of creating
if itemsInCart !=2:
    raise Exception("Items in cart should be greater than Zero")



#seond way of creating exceptions is through assertions

assert(itemsInCart>0)
print("Assertion passed")

'''

try:
    with open("input.txt","r") as f:
        content=f.read()
        print(content)
except Exception as e:
    print("File name is incorrect")
    print(e)

finally:
    print("In finally block")
    f.close()