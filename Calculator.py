import tkinter as tk
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('^', '**')  
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button_labels = [
    ('7', '8', '9', '/', 'sqrt'),
    ('4', '5', '6', '*', '^'),
    ('1', '2', '3', '-', 'factorial'),
    ('0', '.', 'C', '+'),
    ('(', ')', '=')
]


for i in range(len(button_labels)):
    for j in range(len(button_labels[i])):
        label = button_labels[i][j]
        if label == 'C':
            btn = tk.Button(root, text=label, padx=20, pady=20, command=clear, font=('Arial', 12))
        elif label == '=':
            btn = tk.Button(root, text=label, padx=20, pady=20, command=calculate, font=('Arial', 12))
        else:
            if label.isnumeric() or label in ['+', '-', '*', '/', '.', '^', '(', ')']:
                btn = tk.Button(root, text=label, padx=20, pady=20, command=lambda label=label: button_click(label), font=('Arial', 12))
            elif label == 'sqrt':
                btn = tk.Button(root, text=label, padx=16, pady=20, command=lambda: button_click('**0.5'), font=('Arial', 12))
            elif label == 'factorial':
                btn = tk.Button(root, text=label, padx=10, pady=20, command=lambda: button_click('factorial('), font=('Arial', 12))
            else:
                btn = tk.Button(root, text=label, padx=14, pady=20, command=lambda label=label: button_click(math.degrees(math.radians(float(button_click(label))))), font=('Arial', 12))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
