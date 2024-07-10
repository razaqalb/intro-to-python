# You are provided with starter code below that asks you to design a more efficient and functional grade calculating application that is user-friendly and reduces the number of statements written.

# Main topics to include in your design:

# Iteration
# Conditionals
# Functions
# Modularization


def calculate():

    totalsum = 0
    for i in range(5):
        grade = float(input(f"input grade #:{i+1} "))
        totalsum += grade

    average = totalsum / 5

    print ("the average is ", average)

    if average >= 90:
        print("your overall letter grade is an A!")
    elif average >=80 and average <= 89:
        print("your overall letter grade is a B!")
    elif average >=70 and average <=79:
        print("your overall letter grade is a C!")
    elif average >=60 and average <=69:
        print("your overall letter grade is a D!")
    elif average <60:
        print("you have failed.")


calculate()
