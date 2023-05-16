try:
    file = open("input.txt", "r")

    content= file.read()

    print(content)

finally:
    file.close()

