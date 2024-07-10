#discount is determined by age and membership status
# if student (between 12-21) receieves a 30% discount
# if rising adult (22-31) recieves a 15% discount
#if senior (60+) receives a 10% discount
#starting membership costs $180/month
#each membership above goes up by $40
#recurring (6months+) members get a 15% discount more


def main():
    age = int(input("how old are you?"))
    user_input = input("what membership do plan on purchasing?")
    if user_input == 'premium':
        total = 220
    elif user_input =='standard':
        total = 180
    elif user_input == 'exclusive':
        total = 400
    else:
        print("Invalid Membership Type")

    if age <= 21:
        if age <16:
            print("too young to apply") 
            return
        print("your total price is ", total *0.3)
    elif age <= 31:
        print("your total is", total *0.15)
    elif age >60:
        if age >80:
            print("too old to apply")
            return
        print("your total is", total *0.1)
    else:
        print("your total is:", total)
    

main()