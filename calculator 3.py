def main():
    #Option_1()
    Option_2()

def Option_1():
    print("Welcome to the Interactive Python Calculator")
    for i in range(10):
        #num1, num2 = eval(input("enter 2 values"))
        result = eval(input("enter 2 values"))
        print (result)
        if result == 5:
            break

def Option_2():
    print("welcome")
    a = True
    while a:
        result = eval(input("enter 2 values"))
        print(result)
        user_input = input("Do you want to stop the loop (yes or no)?").strip().lower()
        if user_input == 'yes':
            a = False

main()