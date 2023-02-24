from .Point import *
import random
import tkinter as tk
from tkinter import ttk

def generate_random_points(n_dimension):
    temp_point = Point(dimension = n_dimension)
    for j in range (temp_point.dimension):
        temp = random.randint(-10, 10)
        temp_point.coordinates.append(temp)
    return temp_point

def splash_screen_start():
    root = tk.Tk()
    root.geometry("300x200")
    root.overrideredirect(True)
    root.configure(bg = "white") 
    text_label = ttk.Label(root, text = "WELCOME :)", foreground = "black", font = ("Georgia", 14), anchor = "center")
    text_label.pack(pady = 65)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))
    root.after(2000, root.destroy)
    root.mainloop()

def splash_screen_end():
    root = tk.Tk()
    root.geometry("300x200")
    root.overrideredirect(True)
    root.configure(bg = "white") 
    text_label = ttk.Label(root, text = "THANK YOU :)", foreground = "black", font = ("Georgia", 14), anchor = "center")
    text_label.pack(pady = 65)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))
    root.after(2000, root.destroy)
    root.mainloop()