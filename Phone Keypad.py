import tkinter as tk
import random

def keypress(key):
    current_text = number_var.get()
    number_var.set(current_text + key)


def backspace():
    current_text = number_var.get()
    number_var.set(current_text[:-1])


def randomnumber():
    name = name_var.get()
    if name:
        random_number = f"+1 {555}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        number_var.set(random_number)


def call():
    phone_number = number_var.get()
    if phone_number:
        print(f"Calling {phone_number}...")
        call_label.config(text=f"Calling {phone_number}...")


root = tk.Tk()
root.title("Phone Keypad")
root.configure(bg='black')


name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var, font=('Arial', 24))
name_entry.pack(pady=10)


generate_button = tk.Button(root, text="Search Phone Number", command=randomnumber)
generate_button.pack(pady=5)

number_var = tk.StringVar()
number_bar = tk.Entry(root, textvariable=number_var, font=('Arial', 14))
number_bar.pack(pady=10)

keypad_frame = tk.Frame(root,bg='black')
keypad_frame.pack()


keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

def createbutton(text, row, col, command):
    button = tk.Button(keypad_frame, text=text, command=command,background='black')
    button.grid(row=row, column=col, padx=0, pady=2, ipadx=10, ipady=10)

for row_idx, row in enumerate(keys):
    for col_idx, key in enumerate(row):
        createbutton(key, row_idx, col_idx, lambda k=key: keypress(k))


createbutton("Backspace", 4, 1, backspace)



call_button = tk.Button(root, text="Call", command=call)
call_button.pack(pady=10)


call_label = tk.Label(root, text="", font=('Arial', 14), bg='black')
call_label.pack(pady=5)


root.mainloop()