#program that converts celsius temperatures to fahrenheit
#by: razaq albahar

def main():
    celsius()
#   farenheit()
    
# def farenheit():
#  F = eval(input("what is the fahrenheit temperature? "))
#  c = (5/9) * (F - 32)
#  print("the temperature is", c ," degrees celsius.")

def celsius():
 celsius = eval(input("what is the celsius temperature? "))
 fahrenheit = (9/5) * celsius + 32
 print("the temperature is", fahrenheit ," degrees fahrenheit.")

main()