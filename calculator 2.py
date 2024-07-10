def main():
    for i in range (1,11):
        number = int(input("please select a menu option"))
        if number == 1:
            add()
        elif number == 2:
            sub()
        elif number == 3:
            multiply()
        else:
            div()

def add():
    n1 = int(input("please enter the first value:"))
    n2 = int(input("please enter the second value:"))
    result = n1 + n2
    print (" the result is:", result)

def sub():
        n1 =int(input("please enter the first value:"))
        n2 = int(input("please enter the second value:"))
        result = n1 - n2
        print (" the result is:", result)

def multiply():
     n1 = int(input("please enter the first value:"))
     n2 = int(input("please enter the second value:"))
     result = n1 * n2
     print(" the result is:", result)

def div():
     n1 = int(input("please enter the first value:"))
     n2 = int(input("please enter the second value:"))
     result = n1 / n2
     print(" the result is:", result)

main()