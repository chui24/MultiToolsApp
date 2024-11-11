from tkinter import ttk

def apply_styles(root):
    primary_color = "#2C3E50"
    secondary_color = "#1ABC9C"
    text_color = "#ffffff"

    style = ttk.Style()
    style.configure("TButton", background=secondary_color, foreground=text_color, font=("Helvetica", 12, "bold"))
    style.map("TButton", background=[("active", "#16A085")], foreground=[("active", "#f0f4f8")])
    style.configure("TCombobox", fieldbackground=secondary_color, background=secondary_color, foreground=primary_color)
