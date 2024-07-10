for i in range (1,101):
    choice = eval(input("What expression would you like to use?"))
    if choice == 1:
        num1 = int(input("what is your first number you would like to add?"))
        num2 = int(input("what is your second number you would like to add?"))
        print("\nSum:",num1 + num2)

    elif choice == 2:
        num1 = int(input("What is your first number to subtract?"))
        num2 = int(input("what is your second number to subtract?"))
        print("\nSum:", num1-num2)

    elif choice == 3:
        num1 = int(input("what is your first number to multiply?"))
        num2 = int(input("what is your second number to multiply?"))
        print("\nSum:", num1*num2)

    else:
        num1 = int(input("what is your first number to divide?"))
        num2 = int(input("what is your second number to divide?"))


    next_calc = eval(input("do you want another calculation?"))
    if next_calc == "no":
        break
    else:
        print("Invalid Input")