import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


data = [
    ["Date", "Game", "Platform", "Region", "Units Sold", "Revenue"],
    ["2023-01-15", "COD MW", "PC", "North America", 10300, 515000],
    ["2023-01-15", "COD MW 2", "PS4", "Europe", 68384, 3419239],
    ["2023-01-15", "COD MW 3", "Xbox", "Asia", 7717, 347276],
    ["2023-02-28", "COD MW", "PC", "North America", 4697, 234872],
    ["2023-02-28", "COD MW 2", "Xbox", "Europe", 24000, 1200000],
    ["2023-02-28", "COD MW 3", "PS4", "Asia", 12163, 547365],
    ["2023-03-12", "COD MW", "PC", "North America", 18479, 938124],
    ["2023-03-12", "COD MW 2", "Xbox", "Europe", 468468, 2342340],
    ["2023-03-12", "COD MW 3", "PS4", "Asia", 9725, 437635],
    ["2023-04-17", "COD MW", "PC", "North America", 18479, 938124],
    ["2023-04-17", "COD MW 2", "PS4", "Europe", 37935, 1896753],
    ["2023-04-17", "COD MW 3", "Xbox", "Asia", 12541, 564378],
    ["2023-05-19", "COD MW", "PC", "North America", 43344, 650983],
    ["2023-05-19", "COD MW 2", "Xbox", "Europe", 47974, 2398742],
    ["2023-05-19", "COD MW 3", "PS4", "Asia", 7872, 354262],
    ["2023-06-03", "COD MW", "PC", "North America", 16784, 837421],
    ["2023-06-03", "COD MW 2", "PS4", "Europe", 44996, 2249830],
    ["2023-06-03", "COD MW 3", "Xbox", "Asia", 17541, 789387],
    ["2023-07-27", "COD MW", "PC", "North America", 4769, 238472],
    ["2023-07-27", "COD MW 2", "PS4", "Europe", 38567, 1928384],
    ["2023-07-27", "COD MW 3", "PS4", "Asia", 15327, 689734],
    ["2023-08-16", "COD MW", "PC", "North America", 4769, 905847],
    ["2023-08-16", "COD MW 2", "Xbox", "Europe", 40076, 2003847],
    ["2023-08-16", "COD MW 3", "PS4", "Asia", 12082, 543724],
    ["2023-09-24", "COD MW", "PC", "North America", 12673, 632712],
    ["2023-09-24", "COD MW 2", "Xbox", "Europe", 39654, 1982739],
    ["2023-09-24", "COD MW 3", "PS4", "Asia", 19906, 895795],
    ["2023-10-01", "COD MW", "PC", "North America", 12906, 645346],
    ["2023-10-01", "COD MW 2", "Xbox", "Europe", 39998, 1999923],
    ["2023-10-01", "COD MW 3", "PS4", "Asia", 5899, 265472],
    ["2023-11-29", "COD MW", "PC", "North America", 10907, 546375],
    ["2023-11-29", "COD MW 2", "PS4", "Europe", 52919, 2650983],
    ["2023-11-29", "COD MW 3", "Xbox", "Asia", 12858, 578645],
    ["2023-12-30", "COD MW", "PC", "North America", 9149, 457453],
    ["2023-12-30", "COD MW 2", "PS4", "Europe", 55847, 2792384],
    ["2023-12-30", "COD MW 3", "Xbox", "Asia", 15243, 685947],

   
]

file_path = 'gamingcosales.csv'

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("data written to gamingcosales.csv")


df = pd.read_csv('gamingcosales.csv')

df['Date'] = pd.to_datetime(df['Date'])

totalunitsold = df['Units Sold'].sum()
totalrevenue = df['Revenue'].sum()


salesbygame = df.groupby('Game').agg({'Units Sold':'sum', 'Revenue': 'sum'})

averagerevbygame = df.groupby('Game')['Revenue'].mean()


df['Month'] = df['Date'].dt.to_period('M')
monthlysales = df.groupby('Month').agg({'Units Sold': 'sum', 'Revenue': 'sum'})

def human_format(num, pos):

    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.1f%s' % (num, ['', 'K', 'M', 'B', 'T'][magnitude])


#bar graph
fig, ax1 = plt.subplots(figsize=(10, 6))

salesbygame['Units Sold'].plot(kind='bar', ax=ax1, color='b', position=0, width=0.4, label='Units Sold')
ax1.set_xlabel('Game')
ax1.set_ylabel('Units Sold', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_xticks(range(len(salesbygame)))
ax1.set_xticklabels(salesbygame.index, rotation=45)

ax2 = ax1.twinx()
salesbygame['Revenue'].plot(kind='bar', ax=ax2, color='g', position=1, width=0.4, label='Revenue')
ax2.set_ylabel('Revenue', color='g')
ax2.tick_params(axis='y', labelcolor='g')

ax1.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))

fig.suptitle('Sales by Game')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

#line graph

fig, ax = plt.subplots(figsize=(10,6))
for game in df['Game'].unique():
    game_data = df[df['Game']==game].groupby('Month')['Units Sold'].sum()
    ax.plot(game_data.index.to_timestamp(), game_data.values, marker = 'o', label =game)
ax.set_xlabel('Month')
ax.set_ylabel('Units Sold')
ax.set_title('Monthly Sales Trend by Game')
ax.legend()
plt.xticks(rotation=45)
plt.grid(True)


#line graph 2
fig, ax = plt.subplots(figsize = (10,6))
monthlysales['Units Sold'].plot(kind='line', marker='o',ax=ax, color='b', label = 'Units Sold')
ax.set_ylabel('Units Sold', color = 'b')
ax.tick_params(axis='y', labelcolor='b')
ax2=ax.twinx()
monthlysales['Revenue'].plot(kind='line', marker='x', ax=ax2, color ='g', label='Revenue')
ax2.set_ylabel('Revenue', color='g')
ax2.tick_params(axis='y', labelcolor='g')
fig.suptitle('Monthly Sales Trends')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))

plt.tight_layout()
plt.show()
