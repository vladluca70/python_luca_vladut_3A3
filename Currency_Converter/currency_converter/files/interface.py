import tkinter as tk
from tkinter import ttk

def interface(currency_and_values):
    root = tk.Tk()

    root.geometry("800x800")
    root.title("Currency Converter")

    options = []

    for x in currency_and_values:
        options.append(x[0])

    title_label = tk.Label(root, text="Currency Converter", font=("Arial", 24), fg="blue")
    title_label.place(relx=0.5, rely=0.2, anchor="center")

    def show_selections():
        print(f"Name1: {selected_name1.get()}")
        print(f"Name2: {selected_name2.get()}")


    selected_name1 = tk.StringVar(value=options[0])
    selected_name2 = tk.StringVar(value=options[0])

    label_name1 = tk.Label(root, text="From:", font=("Arial", 16))
    label_name1.place(relx=0.3, rely=0.4, anchor="e")
    menu_name1 = tk.OptionMenu(root, selected_name1, *options)
    menu_name1.place(relx=0.4, rely=0.4, anchor="w")

    label_name2 = tk.Label(root, text="To:", font=("Arial", 16))
    label_name2.place(relx=0.3, rely=0.5, anchor="e")
    menu_name2 = tk.OptionMenu(root, selected_name2, *options)
    menu_name2.place(relx=0.4, rely=0.5, anchor="w")

    label_name3 = tk.Label(root, text="Amount:", font=("Arial", 16))
    label_name3.place(relx=0.3, rely=0.6, anchor="e")
    entry_name3 = tk.Entry(root, font=("Arial", 14), width=20)  # Box pentru text
    entry_name3.place(relx=0.4, rely=0.6, anchor="w")

    submit_button = tk.Button(root, text="monede", command=show_selections)
    submit_button.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()