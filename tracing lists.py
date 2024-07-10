for i in range (5):
    prices = [180, 99, 45, 15, 6, 53]
    print(prices)
    num1 = int(input("insert a number: "))
    num2 = int(input("insert another number: "))
    prices.append(num1)
    prices.append(num2)
    print(prices)
    prices.sort()
    print(prices)
    prices.reverse()
    print(prices)
    del (prices [3])
    print (prices)
    num3 = int(input("which number from the list would you like to remove? "))
    if num3 in prices:
        prices.remove(num3)
        print(prices)
        break
    else:
        print("the number you have put in is not in the list.")
        repeat = eval(input("would you like to try again?"))
        if repeat == "no":
            break
        else: print("invalid input")

    
