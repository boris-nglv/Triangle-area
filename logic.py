import math
from tkinter import messagebox

def calculate_triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        raise ValueError("Страните не могат да образуват триъгълник")

def calculate_area_from_entries(entry_a, entry_b, entry_c):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        area = calculate_triangle_area(a, b, c)
        messagebox.showinfo(f"Лицето на триъгълника е {area:.2f}")
    except ValueError as e:
        messagebox.showerror("Грешка", str(e))