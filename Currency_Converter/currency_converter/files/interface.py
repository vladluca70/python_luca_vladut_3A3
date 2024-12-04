import tkinter as tk
from exchange_money import exchange_money

def interface(currency_and_values):
    root = tk.Tk()

    root.geometry("800x800")
    root.title("Currency Converter")

    options = []

    for x in currency_and_values:
        options.append(x[0])

    title_label = tk.Label(root, text="Currency Converter", font=("Arial", 24), fg="blue")
    title_label.place(relx=0.5, rely=0.2, anchor="center")

    def exchange_result():
        name1 = selected_name1.get()
        name2 = selected_name2.get()
        amount = float(entry_name3.get())

        result = exchange_money(amount, name1, name2, currency_and_values)
        result_label.config(text=f"From {name1} to {name2}=> Amount: {result}")

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
    entry_name3 = tk.Entry(root, font=("Arial", 14), width=20)
    entry_name3.place(relx=0.4, rely=0.6, anchor="w")

    submit_button = tk.Button(root, text="Convert", command=exchange_result)
    submit_button.place(relx=0.5, rely=0.7, anchor="center")

    result_label = tk.Label(root, text="", font=("Arial", 16), fg="green")
    result_label.place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()