import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Button, filedialog #Obtain the complete route of the archive 
import os

root = tk.Tk() #Create a object

root.geometry("400x400") #The size of the window

root.title("VisualAP") #The name of it

root.iconbitmap("C:/Users/Erik/Desktop/GUI_Final_Project/Icon/Logo.ico") #This is the icon of alatoo universtity

button1 = tk.Button(root, text='Press Me')
button1.pack()

tk.mainloop()
