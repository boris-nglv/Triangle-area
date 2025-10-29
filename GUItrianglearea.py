import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            messagebox.showinfo("Резултат", f"Лицето на триъгълника е {area:.2f}")
        else:
            messagebox.showerror("Грешка", "Страните не могат да образуват триъгълник!")
    except ValueError:
        messagebox.showerror("Грешка", "Моля, въведи числа!")

root = tk.Tk()
root.title("Лице на триъгълник")

tk.Label(root, text="Страна a:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Страна b:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Страна c:").grid(row=2, column=0, padx=10, pady=5)

entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_c = tk.Entry(root)

entry_a.grid(row=0, column=1, padx=10, pady=5)
entry_b.grid(row=1, column=1, padx=10, pady=5)
entry_c.grid(row=2, column=1, padx=10, pady=5)

button = tk.Button(root, text="Сметни", command=calculate_area, bg="#4CAF50", fg="white", font=("Arial", 12))
button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()