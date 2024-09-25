# CALCULATOR

import tkinter as tk

# Function to update the expression in the text entry box
def update_expression(symbol):
    expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression + str(symbol))

# Function to calculate the result of the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Create the entry box for displaying the expression and result
entry = tk.Entry(root, width=20, font=('Arial', 24), bd=10, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=calculate)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18),
                        command=lambda b=button: update_expression(b))
    
    btn.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)
clear_button.grid(row=row_val, column=col_val, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
