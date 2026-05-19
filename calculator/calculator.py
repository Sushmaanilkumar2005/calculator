from tkinter import *

# Window
root = Tk()
root.title("GUI Calculator")
root.geometry("350x500")
root.configure(bg="black")

# Input box
entry = Entry(root,
              width=26,
              font=("Arial", 30),
              bd=18,
              relief=RIDGE,
              justify=RIGHT,
              bg="white",
              fg="black")

entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button click function
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(num))

# Clear function
def clear():
    entry.delete(0, END)

# Equal function
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Button design
btn_font = ("Arial", 18, "bold")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

# Create buttons
for (text, row, col) in buttons:

    if text == "=":
        Button(root,
               text=text,
               width=6,
               height=2,
               font=btn_font,
               bg="orange",
               fg="white",
               command=equal).grid(row=row, column=col, padx=5, pady=5)

    else:
        Button(root,
               text=text,
               width=6,
               height=2,
               font=btn_font,
               bg="gray",
               fg="white",
               command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
Button(root,
       text="C",
       width=28,
       height=2,
       font=("Arial", 14, "bold"),
       bg="red",
       fg="white",
       command=clear).grid(row=5, column=0, columnspan=4, pady=10)

# Run app
root.mainloop()