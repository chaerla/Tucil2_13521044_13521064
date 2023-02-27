from .Point import *
from mpl_toolkits.mplot3d import Axes3D
from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import random
import platform
import psutil

def generate_random_points(n_dimension):
    temp_point = Point(dimension = n_dimension)
    for j in range (temp_point.dimension):
        temp = random.uniform(-10, 10)
        temp_point.coordinates.append(temp)
    return temp_point

def splash_screen():
    root = tk.Tk()
    root.geometry("300x200")
    root.overrideredirect(True)
    root.configure(bg = "white")  
    text_label = ttk.Label(root, text = "WELCOME! :)", foreground = "black", font = ("Georgia", 24))
    text_label.pack(pady = 65)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))
    root.after(2000, root.destroy)
    root.mainloop()

def show_plotter(point_list, point_1, point_2):
    """
    prereq: dimension must be 3
    """
    figure = plt.figure()
    ax = figure.add_subplot(111, projection='3d')
    x = [point[0] for point in point_list]
    y = [point[1] for point in point_list]
    z = [point[2] for point in point_list]

    colors = ['red' if (point == point_1 or point == point_2) else 'blue' for point in point_list]
    ax.scatter(x, y, z, c = colors)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def get_num_of_points():
    """
    asks for the num of points and validates if it's an integer
    """
    while True:
        try:
            num_of_points = int(input("Enter the number of points: "))
            if num_of_points > 1:
                return num_of_points
            print("The number of points must be larger than 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_dimension():
    """
    asks for the dimension and validates if it's an integer
    """
    while True:
        try:
            dimension = int(input("Enter the dimension of the points: "))
            return dimension
        except ValueError:
            print("Invalid input. Please enter an integer.")

def print_computer_spec():
    print("This program is being run on a computer with this specification:")
    # get the system information
    system = platform.uname()

    # get the CPU information
    cpu = platform.processor()

    # get the memory information
    memory = psutil.virtual_memory()
    print("System: {} {}".format(system.system, system.release))
    print("Node name: {}".format(system.node))
    print("CPU: {}".format(cpu))
    print("Memory: {} MB".format(memory.total / (1024*1024)))
    