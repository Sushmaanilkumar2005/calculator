import tkinter as tk
import math

# Create window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x600")
root.configure(bg="black")

# Input field
entry = tk.Entry(root,
                 width=22,
                 font=("Arial", 24),
                 bd=10,
                 relief=tk.RIDGE,
                 justify="right",
                 bg="white")

entry.grid(row=0, column=0, columnspan=5, pady=20)

# Function to insert values
def click(value):
    entry.insert(tk.END, value)

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Scientific functions
def sin():
    value = float(entry.get())
    result = math.sin(math.radians(value))
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def cos():
    value = float(entry.get())
    result = math.cos(math.radians(value))
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def tan():
    value = float(entry.get())
    result = math.tan(math.radians(value))
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def sqrt():
    value = float(entry.get())
    result = math.sqrt(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def log():
    value = float(entry.get())
    result = math.log10(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def square():
    value = float(entry.get())
    result = value ** 2
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Button style
btn_font = ("Arial", 14, "bold")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3)
]

# Create normal buttons
for (text, row, col) in buttons:

    if text == "=":
        tk.Button(root,
                  text=text,
                  width=6,
                  height=2,
                  bg="orange",
                  fg="white",
                  font=btn_font,
                  command=calculate).grid(row=row, column=col, padx=5, pady=5)

    else:
        tk.Button(root,
                  text=text,
                  width=6,
                  height=2,
                  bg="gray",
                  fg="white",
                  font=btn_font,
                  command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5)

# Scientific buttons
tk.Button(root, text="sin", width=6, height=2,
          bg="blue", fg="white", font=btn_font,
          command=sin).grid(row=5, column=0)

tk.Button(root, text="cos", width=6, height=2,
          bg="blue", fg="white", font=btn_font,
          command=cos).grid(row=5, column=1)

tk.Button(root, text="tan", width=6, height=2,
          bg="blue", fg="white", font=btn_font,
          command=tan).grid(row=5, column=2)

tk.Button(root, text="√", width=6, height=2,
          bg="green", fg="white", font=btn_font,
          command=sqrt).grid(row=5, column=3)

tk.Button(root, text="log", width=6, height=2,
          bg="purple", fg="white", font=btn_font,
          command=log).grid(row=6, column=0)

tk.Button(root, text="x²", width=6, height=2,
          bg="purple", fg="white", font=btn_font,
          command=square).grid(row=6, column=1)

tk.Button(root, text="π", width=6, height=2,
          bg="purple", fg="white", font=btn_font,
          command=lambda: click(str(math.pi))).grid(row=6, column=2)

tk.Button(root, text="C", width=6, height=2,
          bg="red", fg="white", font=btn_font,
          command=clear).grid(row=6, column=3)

# Run app
root.mainloop()