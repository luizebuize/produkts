import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        value = float(entry.get())
    except:
        messagebox.showerror("Kļūda", "Ievadi skaitli!")
        return

    from_unit = from_var.get()
    to_unit = to_var.get()

    if from_unit == to_unit:
        result = value
    elif from_unit == "Metri" and to_unit == "Pēdas":
        result = value * 3.28084
    elif from_unit == "Pēdas" and to_unit == "Metri":
        result = value / 3.28084
    elif from_unit == "Kilogrami" and to_unit == "Mārciņas":
        result = value * 2.20462
    elif from_unit == "Mārciņas" and to_unit == "Kilogrami":
        result = value / 2.20462
    elif from_unit == "Kilometri" and to_unit == "Jūdzes":
        result = value * 0.621371
    elif from_unit == "Jūdzes" and to_unit == "Kilometri":
        result = value / 0.621371
    else:
        messagebox.showerror("Kļūda", "Nederīga konversija!")
        return

    result = round(result, 2)
    result_label.config(text=f"Rezultāts: {result}")

    history.insert(0, f"{value} {from_unit} → {result} {to_unit}")
    update_history()

def update_history():
    history_list.delete(0, tk.END)
    for item in history:
        history_list.insert(tk.END, item)

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Rezultāts:")

root = tk.Tk()
root.title("Unit Converter")

history = []

entry = tk.Entry(root, width=30)
entry.pack()

units = ["Metri", "Pēdas", "Kilogrami", "Mārciņas", "Kilometri", "Jūdzes"]

from_var = tk.StringVar(value=units[0])
to_var = tk.StringVar(value=units[1])

from_menu = tk.OptionMenu(root, from_var, *units)
from_menu.pack()

to_menu = tk.OptionMenu(root, to_var, *units)
to_menu.pack()

btn_convert = tk.Button(root, text="Pārveidot", command=convert)
btn_convert.pack()

btn_clear = tk.Button(root, text="Notīrīt", command=clear)
btn_clear.pack()

result_label = tk.Label(root, text="Rezultāts:")
result_label.pack()

history_list = tk.Listbox(root, width=40)
history_list.pack()

root.mainloop()