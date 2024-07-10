import csv
from graphics import *

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def main():
    win = GraphWin("Temperature Converter", 500, 300)
    win.setBackground("lightgray")

    # Celsius Entry
    celsius_text = Text(Point(80, 50), "Celsius:")
    celsius_text.draw(win)
    celsius_entry = Entry(Point(200, 50), 5)
    celsius_entry.draw(win)

    # Fahrenheit Entry
    fahrenheit_text = Text(Point(80, 100), "Fahrenheit:")
    fahrenheit_text.draw(win)
    fahrenheit_entry = Entry(Point(200, 100), 5)
    fahrenheit_entry.draw(win)

    # Convert Button
    convert_button = Rectangle(Point(100, 150), Point(200, 180))
    convert_button.setFill("lightblue")
    convert_button.draw(win)
    convert_text = Text(Point(150, 165), "Convert")
    convert_text.draw(win)

    # Create and open the CSV file for writing
    with open('temperature_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Celsius', 'Fahrenheit'])  # Write header
        
        # Conversion Loop
        while True:
            click_point = win.getMouse()

            # Check if click is within button bounds
            if 100 <= click_point.getX() <= 200 and 150 <= click_point.getY() <= 180:
                try:
                    celsius = float(celsius_entry.getText())
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    fahrenheit_entry.setText(str(fahrenheit))
                    
                    # Write the data to the CSV file
                    writer.writerow([celsius, fahrenheit])
                except ValueError:
                    fahrenheit_entry.setText("Invalid Input")
            
            # Close the window and break the loop
            elif 200 <= click_point.getX() <= 300 and 0 <= click_point.getY() <= 200:
                win.close()
                break

if __name__ == "__main__":
    main()
