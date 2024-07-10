# July 1 Morning Task - Review
# Visualizing Data

# Add 2 Additional Exercises and Mileage
# Write the data to a CSV file
# Read from CSV
# Describe() the DataFrame
# Visualize the data as a Bar Chart
# Visualize the data as a Line Chart
# Visualize as a Pie Chart
# Visualize as Histogram



import pandas as pd
import matplotlib.pyplot as plt

dict1 = {'exercises': ['Running','Walking','Cycling','Swimming','Hiking'],
         'mileage': [250, 1000, 550,300,400]}
df = pd.DataFrame(dict1)

df.to_csv('workouts.csv', index=False)


df_read=pd.read_csv('workouts.csv')

print("\nSummary statistics:")
print(df.describe())

# bar chart
plt.figure(figsize=(8,5))
plt.bar(df_read['exercises'], df_read['mileage'], color='skyblue')
plt.title('mileage by exercise')
plt.xlabel('exercises')
plt.ylabel('mileage')
plt.grid(True)
plt.show()


#line chart
plt.figure(figsize=(8,5))
plt.plot(df_read['exercises'], df_read['mileage'], marker='o', linestyle='-',color='royalblue')
plt.title('mileage by exercise')
plt.xlabel('exercises')
plt.ylabel('mileage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# pie chart
df.set_index('exercises').plot(kind='pie', y='mileage', x='exercises', autopct='%1.1f',legend=False, title='mileage by exercise')
plt.ylabel('')
plt.show()


