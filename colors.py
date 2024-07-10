def main():
    colors = ['red', 'blue', 'green']
    print (colors [0])
    print (colors [1])
    print (colors [2])
    print()
    print (colors, "this is the original list")
    print()
    print(len(colors), "is the length of the list")
    new_color = input("enter an item to add to the list: ")
    colors.append(new_color)
    print(colors)
    colors.sort()
    print(colors)
    colors.reverse()
    print(colors)

main()

