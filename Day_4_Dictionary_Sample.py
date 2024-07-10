
#  Day 4 - Morning Session

#  Dictionary Sample

import time

print()
print("- Original Dictionary")
country_capitals = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "Manchester"}
print(country_capitals)
print()
input("Press Enter to continue...")
print()

print("- Add and Display New key/value Pair of Japan:Tokyo")
country_capitals["Japan"] = "Tokyo" 
print("Updated Dictionary: ",country_capitals)
print()
input("Press Enter to continue...")
print()

print("- Delete the key/value Pair, Italy:Rome")
del country_capitals["Italy"] 
print("Updated Dictionary: ",country_capitals)
print()
input("Press Enter to continue...")
print()

print("- Add the key/value Pair, England:London") 
country_capitals["England"] = "London"
print("Updated Dictionary: ",country_capitals)
print()
input("Press Enter to continue...")
print()

print("- Access and Display an Element")
print("The capital of Nepal is: ", country_capitals["Nepal"]) # prints Kathmandu
input("Press Enter to continue...")
print()

print()
print("- The in Keyword Verifies if an Element Exists and Prints TRUE")
print("--------------------------------------------------------------")
print("England" in country_capitals) # Prints TRUE
input("Press Enter to continue...")
print()

print("- Print the length of the Dictionary")
length = len(country_capitals)
print(length)
print()
input("Press Enter to continue...")
print()

print ("- Prints the SORTED Keys - This is TEMPORARY ")
sorted_countries = sorted(country_capitals)
print(sorted_countries)
print()
input("Press Enter to continue...")
print()

print("- Print the UNSORTED Values in the Dictionary") 
print("Return the dictionary values: ", country_capitals.values())
input("Press Enter to continue...")
print()

print()
print("- TRICKY - Sort Dictionary key/values based on")
print("- the VALUE at index 1 of each element")
print("- BUT return as Tuple Pairs in a List")
print("- This Process Uses a LAMBDA Function")
print("- The x:x[1]  # The 1 Instructs a VALUE First Sort")
print("- The List is NOT Permanently Changed!!")
print()
sorted_country_values = sorted(country_capitals.items(), key=lambda x:x[1])
print("A - Z: ", sorted_country_values)
print()
print("- Sort based on KEYS")
print()
sorted_country_values = sorted(country_capitals.items(), key=lambda x:x[0])
print("A - Z: ", sorted_country_values)
print()
input("Press Enter to continue...")
print()

print("- Now convert back into a Dictionary")
converted_dict = dict(sorted_country_values)
print("Convert List to Dictionary ", converted_dict)
print()
input("Press Enter to continue...")
print()

print("- Use the LAMBDA Function to Reverse Sort Based on VALUES")  
sorted_country_values = sorted(country_capitals.items(), key=lambda x:x[1], reverse = True)
print("Z - A: ", sorted_country_values)
print()
input("Press Enter to continue...")
print()

print()
print(" - And Now Convert Back Into a Dictionary")
converted_dict = dict(sorted_country_values)
print("Convert List to Dictionary ", converted_dict)
print()
input("Press Enter to continue...")
print()

print("- Iterate Through the Dictionary")
print()
for key in country_capitals : 
    print("Iterate ORIGINAL Dictionary Values: ", country_capitals [key])
print()
for key in country_capitals : 
    print("Iterate ORIGINAL Dictionary Keys + Values: ", key, country_capitals [key])
print()
input("Press Enter to continue...")
print()

print("- Use an If Conditional to Check if a Value Exists")
for key in country_capitals :
    if ("London"):
        print("London is the capital of England")
        break
print()
input("Press Enter to continue...")
print()

print("- Search for a Key in the Dictionary")
country = str(input("Which country are you looking for? "))
for key in country_capitals :
    if key == country:
        print(country, "is found in the Dictionary")
        break

