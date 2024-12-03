import tkinter as tk
from tkinter import ttk

def interface():
    lista1=['lei', 'euro']
    lista2=['usd', 'chf']

    root = tk.Tk()
    root.title("Currency Converter")

    chenar = ttk.LabelFrame(root, text="Currency Converter", padding=(90, 90))
    chenar.grid(row=0, column=0, padx=90, pady=90)

    buton = ttk.Button(chenar, text="Convert")
    buton.grid(row=0, column=0, padx=50, pady=100)


    root.mainloop()