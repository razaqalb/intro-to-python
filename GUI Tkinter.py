#  Day 6 - Morning Session

#  Tkinter Library GUI


import tkinter as tk

def on_button_click():
    user_input = entry.get()
    label_result.config(text="Hello, " + user_input + "!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI Example")

# Create and add widgets
label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# Run the main event loop
root.mainloop()
