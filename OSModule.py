import os
import shutil as sh

print("Current working directory-->",os.getcwd())

print("Switching to directory-->",os.chdir("C:\\Users\\yuvar\\PycharmProjects\\dictionary"))

print("Fetching the path after changing the directory-->",os.getcwd())

print("Switching to directory-->",os.chdir("C:\\Users\\yuvar\\PycharmProjects\\pythonProject"))

print(os.listdir("C:\\Users\\yuvar\\PycharmProjects\\pythonProject"))

#os.mkdir("test")

#os.rename("test_new","test")
#os.rename("C:\\Users\\yuvar\\PycharmProjects\\pythonProject\\test","C:\\Users\\yuvar\\PycharmProjects\\pythonProject\\test_new")

#os.remove("C:\\Users\\yuvar\\PycharmProjects\\pythonProject\\1.py")

#os.rmdir("test")

sh.rmtree("test")

