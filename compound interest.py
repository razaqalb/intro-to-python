#Create a program that calculates the future value of an investment using compound interest.
    
#Calculate the compound interest using the formula:
#A = P * (1 + r/n)^(nt)
   

#    where:
#     A = the future value of the investment/loan, including interest
#     P = the principal investment amount (initial amount)
#     r = the annual interest rate (in decimal)
#     n = the number of times that interest is compounded per unit 't' (e.g., annually, semi-annually)
#     t = the time the money is invested/borrowed for, in years

import math

def compound_interest(principal, rate, time):

    n = 12 #(compounded 12 months a year)
    return principal *math.pow(1+(rate/n), n* time)

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("enter the annual interest rate in decimal: "))
    time = float(input("enter the time the money is invested for (in years)"))

    future_value = compound_interest(principal,rate,time)
    print("the future value of the investment is ${:.2f}".format(future_value))

if __name__ == "__main__":
    main()