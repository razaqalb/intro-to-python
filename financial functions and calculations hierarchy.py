def main ():
    get_input()
    

def get_input():
    hours_worked = int(input("how many hours have you worked? "))
    payment_per_hour = int(input("How much money did you recieve for working during this hours? "))

    overtime_rate = 1.5
    regular_hours = 40

    if hours_worked <= regular_hours:
        gross_pay = hours_worked * payment_per_hour
    else:
        regularpay = hours_worked * payment_per_hour
        allhrs = hours_worked - regular_hours
        overtime_pay = allhrs * overtime_rate * payment_per_hour
        gross_pay = overtime_pay + regularpay
    print("you have worked", hours_worked,"hours and have earned", gross_pay)
    calc_withholdings(gross_pay)

def calc_withholdings(gross_pay):
    net_pay = gross_pay - (gross_pay * 0.04) 
    print ("after tax, your net pay is: ", net_pay)
    
main()