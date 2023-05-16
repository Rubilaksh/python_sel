with open("message.txt","w") as w:
    content=["first line", "\nsecond line", "\nthird line"]
    w.writelines(content)