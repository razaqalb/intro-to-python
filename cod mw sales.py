import csv
import pandas as pd
import matplotlib.pyplot as plt

# Data to be written to CSV
data = [
    ['month', 'salesvol', 'salesvalue', 'gamename'], 
    [1, 200000, 59.99, 'call of duty: MW'],
    [2, 1700000, 59.99, 'call of duty: MW'],
    [3, 1300000, 59.99, 'call of duty: MW'],
    [4, 1500000, 59.99, 'call of duty: MW'],
    [5, 1293040, 59.99, 'call of duty: MW'],
    [6, 983000, 59.99, 'call of duty: MW'],
    [7, 734209, 59.99, 'call of duty: MW'],
    [8, 1109845, 59.99, 'call of duty: MW'],
    [9, 834098, 59.99, 'call of duty: MW'],
    [10, 1123890, 44.99, 'call of duty: MW'],
    [11, 1409393, 44.99, 'call of duty: MW'],
    [12, 865342, 44.99, 'call of duty: MW'],
]

# Writing data to CSV
with open('cod_mw_sales.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to cod_mw_sales.csv successfully")

# Reading data from CSV
data = pd.read_csv('cod_mw_sales.csv')

# Creating a line chart of sales volume per month
plt.figure(figsize=(10,6))
plt.plot(data['month'], data['salesvol'], marker='o', linestyle='-', color='b')
plt.xlabel('Month')
plt.ylabel('Sales Volume')
plt.title('Monthly Sales Volume for Call of Duty: Modern Warfare')
plt.xticks(data['month'])
plt.grid(True)
plt.tight_layout()

plt.show()
