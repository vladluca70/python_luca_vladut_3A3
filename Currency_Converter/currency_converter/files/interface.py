import tkinter as tk
from tkinter import ttk

def interface():
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Currency Converter")

    title_label = tk.Label(root, text="Currency Converter", font=("Arial", 24), fg="blue")

    title_label.place(relx=0.5, rely=0.1, anchor="center")

    root.mainloop()