def calc_sum(numbers):
    return sum(numbers)
def calc_div(numbers):
    return sum(numbers)/len(numbers)
def calc_multip(numbers):
    return sum(numbers)*len(numbers)
def calc_max(numbers):
    return max(numbers)

def main():
    numbers = []
    print("Please enter 15 numbers:")
    for i in range(15):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    sum = calc_sum(numbers)
    quotient = calc_div(numbers)
    product = calc_multip(numbers)
    max = calc_max(numbers)

    print("the sum is: ", sum)
    print(f"the quotient is: {quotient:2f}")
    print("the product is: ", product)
    print("the max is: ", max)
    

main()