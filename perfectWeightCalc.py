import tkinter as tk
from tkinter import ttk, messagebox

def calculate_ideal_weight():
    try:
        gender = gender_var.get()
        height = float(height_entry.get())

        if height <= 0:
            raise ValueError("Height must be a positive number.")

        if gender == "Male":
            ideal_weight = 50 + 0.9 * (height - 152)
        elif gender == "Female":
            ideal_weight = 45.5 + 0.9 * (height - 152)
        else:
            messagebox.showerror("Input Error", "Please select a gender.")
            return

        result_label.config(text=f"Ideal Weight: {ideal_weight:.2f} kg (Devine Formula)")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid height.")

def clear_fields():
    height_entry.delete(0, tk.END)
    gender_var.set('')
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Ideal Weight Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Height input
tk.Label(root, text="Enter your height (cm):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

# Gender selection
tk.Label(root, text="Select Gender:").pack(pady=5)
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], state="readonly")
gender_dropdown.pack()

# Buttons
tk.Button(root, text="Calculate", command=calculate_ideal_weight).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

# Run the GUI loop
root.mainloop()
