from math import factorial


def main():
    Factorial = int(input("What number do you want to factor? "))
    Result = factorial(Factorial)   
    print("the factorial of", Factorial, "is:", Result)

main()