def main():
    number = int(input("Enter Factorial"))
    factorial(number)
    print("the factorial of", number, "is:", factorial(number))
    
def factorial (n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)
    
main()