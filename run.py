"""
This files contains the main call to run the application 

author: chuimachado (chuimachado@gmail.com)
developed at: November 2024
"""

from app.main import InterfaceApp
import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
app = InterfaceApp(root)
root.mainloop()
