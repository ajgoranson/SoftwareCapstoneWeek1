classes = []

class_name = input('Enter class name, Press Enter to quit. ')

while class_name:
    classes.append(class_name)
    class_name = input('Enter class name, Press enter to quit. ')


for x in classes:
    print(x)
