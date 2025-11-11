import tkinter as tk
from logic import calculate_area_from_entries

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

button = tk.Button(
    root, text="Сметни", command=lambda: calculate_area_from_entries(entry_a, entry_b, entry_c), bg="#4CAF50", fg="white", font=("Arial", 12))
button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()