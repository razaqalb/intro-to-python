import csv
import pandas as pd
import matplotlib.pyplot as plt

# Data to be written to CSV
data = [
    ['employeeid', 'firstname', 'lastname', 'department', 'salary'],
    [1, 'john', 'doe', 'engineering', 75000],
    [2, 'jane', 'smith', 'marketing', 68000],
    [3, 'bob', 'johnson', 'sales', 72000],
    [4, 'alice', 'williams', 'HR', 65000],
    [5, 'michael', 'brown', 'IT', 78000]
]

# Writing data to CSV
with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to employees.csv successfully")

# Reading data from CSV
data = pd.read_csv('employees.csv')

print(data)

# Creating a pie chart of employee salaries
plt.figure(figsize=(10,6))
plt.pie(data['salary'], labels=data['firstname'] + ' ' + data['lastname'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Employee Salaries')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
