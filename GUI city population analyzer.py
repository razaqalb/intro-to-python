from tkinter import filedialog, messagebox
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt


def csv():
    global df

    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        messagebox.showinfo("Info", "CSV file loaded successfully!")
        print(df.columns)


def filterplot():

    filter_value = filter_value_entry.get()
    filtered_df = df[df['Country'].str.lower() == filter_value.lower()]

    top_5_cities = filtered_df.nlargest(5, 'Population')
    
    top_5_cities = top_5_cities.sort_values(by='Population', ascending=False)
    top_5_cities.set_index('City', inplace=True)
    
    total_population = top_5_cities['Population'].sum()
    percentages = (top_5_cities['Population'] / total_population) * 100
    
    if top_5_cities.empty:
        messagebox.showerror("Error", "No data available to plot.")
        return
    
    plt.figure(figsize=(10, 7))
    plt.pie(percentages, labels=top_5_cities.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Top 5 Most Populated Cities in {filter_value}')
    plt.show()

    plt.figure(figsize=(10, 7))
    top_5_cities['Population'].plot(kind='bar')
    plt.ylabel('Population')
    plt.title(f'Top 5 Most Populated Cities in {filter_value}')
    plt.xticks(rotation=45)
    plt.ticklabel_format(style='plain', axis='y')  
    plt.tight_layout()
    plt.show()


root = tk.Tk()
root.title("City Population Analyzer")
root.configure(bg='lightblue')

load_button = tk.Button(root, text="Load CSV", command=csv, bg='lightblue')
load_button.grid(row=0, column=0, padx=10, pady=10)

filter_value_label = tk.Label(root, text="Filter Country:", bg='lightblue')
filter_value_label.grid(row=1, column=0, padx=10, pady=10)

filter_value_entry = tk.Entry(root, bg='gray13')
filter_value_entry.grid(row=1, column=1, padx=10, pady=10)

plot_button = tk.Button(root, text="Plot Top 5 Cities", command=filterplot, bg='lightblue')
plot_button.grid(row=2, column=0, columnspan= 2,pady=10)

root.eval('tk::PlaceWindow . center')
root.mainloop()
