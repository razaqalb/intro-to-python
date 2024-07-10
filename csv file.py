import csv
import pandas as pd
import matplotlib.pyplot as plt




data = [
    ['employeeid', 'firstname', 'lastname','department', 'salary'],
    [1, 'john', 'doe', 'engineering', 75000],
    [2, 'jane', 'smith', 'marketing', 68000],
    [3, 'bob', 'johnson', 'sales', 72000],
    [4, 'alice', 'williams', 'HR', 65000],
    [5, 'michael', 'brown', 'IT', 78000]
]

with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("data written to employees.csv as successfully")


data = pd.read_csv('employees.csv')


print(data)

plt.figure(figsize=(10,6))
plt.bar(data['firstname'] + ' ' + data['lastname'], data['salary'], color='skyblue')
plt.xlabel('employee')
plt.ylabel('salary')
plt.title('employee salaries')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()