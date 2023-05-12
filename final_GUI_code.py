import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/Users/perrytraore/Documents/GitHub/ST1_capstone_project/resources_for _my_code/auto-mpg.csv')

# Create the main window
window = tk.Tk()
window.title("ST1 Capstone Project")
window.geometry("800x600")

# Load and display the background image
background_image = ImageTk.PhotoImage(Image.open('/Users/perrytraore/Documents/GitHub/ST1_capstone_project/resources_for _my_code/mustang1.tiff'))
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a title label to the GUI
title_label = tk.Label(window, text="ST1 Capstone Project\nVehicle Information", font=("Times New Roman", 25, "bold"), fg="#ff0000", bg="#333333")
title_label.pack(pady=10)

# Define styles for the buttons
button_style = ttk.Style()
button_style.configure('TButton', background='#000000', foreground='#ff0000', font=('Times New Roman', 12, 'bold'))

# Function to plot the distribution of MPG values
def plot_mpg_distribution():
    plt.hist(df['mpg'], bins=20, edgecolor='k', color='#ff0000')
    plt.xlabel('MPG)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Distribution of MPG', fontsize=14, fontweight='bold')
    plt.show()

# Create a button to plot the distribution of MPG
mpg_distribution_button = ttk.Button(window, text="Distribution of MPG", command=plot_mpg_distribution, style='TButton')
mpg_distribution_button.pack(pady=10)

# Function to plot MPG vs. Origin
def plot_mpg_vs_origin():
    plt.figure()
    sns.boxplot(x='origin', y='mpg', data=df, color='#ff0000')
    plt.xlabel('Origin', fontsize=12)
    plt.ylabel('MPG', fontsize=12)
    plt.title('MPG vs. Origin', fontsize=14, fontweight='bold')
    plt.show()

# Create a button to plot MPG vs. Origin
mpg_vs_origin_button = ttk.Button(window, text="MPG vs. Origin", command=plot_mpg_vs_origin, style='TButton')
mpg_vs_origin_button.pack(pady=10)

# Function to plot MPG vs. Cylinders
def plot_mpg_vs_cylinders():
    plt.figure()
    sns.scatterplot(x='cylinders', y='mpg', data=df, color='#ff0000')
    plt.xlabel('Cylinders', fontsize=12)
    plt.ylabel('MPG', fontsize=12)
    plt.title('MPG vs. Cylinders', fontsize=14, fontweight='bold')
    plt.show()

# Create a button to plot MPG vs. Cylinders
mpg_vs_cylinders_button = ttk.Button(window, text="MPG vs. Cylinders", command=plot_mpg_vs_cylinders, style='TButton')
mpg_vs_cylinders_button.pack(pady=10)

# Function to plot MPG vs. Horsepower
def plot_mpg_vs_horsepower():
    plt.figure()
    sns.scatterplot(x='horsepower', y='mpg', data=df, color='#ff0000')
    plt.xlabel('Horsepower', fontsize=12)
    plt.ylabel('MPG', fontsize=12)
    plt.title('MPG vs. Horsepower', fontsize=14, fontweight='bold')
    plt.show()

# Create a button to plot MPG vs. Horsepower
mpg_vs_horsepower_button = ttk.Button(window, text="MPG vs. Horsepower", command=plot_mpg_vs_horsepower, style='TButton')
mpg_vs_horsepower_button.pack(pady=10)

# Function to plot MPG vs. Weight
def plot_mpg_vs_weight():
    plt.figure()
    sns.scatterplot(x='weight', y='mpg', data=df, color='#ff0000')
    plt.xlabel('Weight', fontsize=12)
    plt.ylabel('MPG', fontsize=12)
    plt.title('MPG vs. Weight', fontsize=14, fontweight='bold')
    plt.show()

# Create a button to plot MPG vs. Weight
mpg_vs_weight_button = ttk.Button(window, text="MPG vs. Weight", command=plot_mpg_vs_weight, style='TButton')
mpg_vs_weight_button.pack(pady=10)


# Function to close the currently displayed graph
def close_graph():
    plt.close()

# Create a button to close the currently displayed graph
close_button = ttk.Button(window, text="Close Graph", command=close_graph, style='TButton')
close_button.pack(pady=10)

# Function to close the program
def close_program():
    window.destroy()

# Create a button to close the program
close_button = ttk.Button(window, text="Close Program", command=close_program, style='TButton')
close_button.pack(pady=10)

# Program description
program_description = """This program analyzes vehicle information from a dataset called 'auto-mpg.csv'.
It provides visualizations and insights related various vehicle attributes such as origin, cylinders, horsepower, and weight.

How to use:
1. Click on the desired graph.
2. Use the 'Close Graph' button to close the currently displayed graph.
3. To exit the program, click on the 'Close Program' button."""

# Create a text box for program description
description_textbox = tk.Text(window, width=70, height=10, font=("Times New Roman", 10), fg="#bfbdbd", bg="#080808")
description_textbox.insert(tk.END, program_description)
description_textbox.pack(pady=10)

# Run the GUI
window.mainloop()

