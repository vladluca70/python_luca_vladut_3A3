import tkinter as tk
from tkinter import ttk

def interface():
    lista1 = ['lei', 'euro']
    lista2 = ['usd', 'chf']

    # Crearea ferestrei principale
    root = tk.Tk()
    root.title("Currency Converter")

    # Crearea unui chenar pentru conținut
    chenar = ttk.LabelFrame(root, text="Currency Converter", padding=(20, 20))
    chenar.grid(row=0, column=0, padx=20, pady=20)

    # Setăm stilul pentru Combobox pentru a modifica culorile
    style = ttk.Style()
    style.configure("TCombobox",
                    fieldbackground="white",  # fundal alb pentru combobox
                    background="white",  # fundal alb pentru butonul dropdown
                    foreground="black")  # text negru

    # Dropdown pentru currency1
    ttk.Label(chenar, text="Select Currency 1:").grid(row=0, column=0, pady=10, sticky="w")
    currency1 = ttk.Combobox(chenar, values=lista1, state="readonly", style="TCombobox")
    currency1.grid(row=0, column=1, pady=10)
    currency1.current(0)  # Setăm valoarea inițială

    # Dropdown pentru currency2
    ttk.Label(chenar, text="Select Currency 2:").grid(row=1, column=0, pady=10, sticky="w")
    currency2 = ttk.Combobox(chenar, values=lista2, state="readonly", style="TCombobox")
    currency2.grid(row=1, column=1, pady=10)
    currency2.current(0)  # Setăm valoarea inițială

    # Buton pentru conversie
    buton = ttk.Button(chenar, text="Convert")
    buton.grid(row=2, column=0, columnspan=2, pady=20)

    # Rularea interfeței grafice
    root.mainloop()