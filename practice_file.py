with open("file_practice.txt","w") as w:
    message= ["no1", "\nno2", "\nno3"]
    w.writelines(message)