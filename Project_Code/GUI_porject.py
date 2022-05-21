import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Button, filedialog #Obtain the complete route of the archive 
import os

root = tk.Tk() #Create a object

root.geometry("400x400") #The size of the window

root.title("VisualAP") #The name of it

root.iconbitmap("C:/Users/Erik/Desktop/GUI_Final_Project/Icon/Logo.ico") #This is the icon of alatoo universtity

l=tk.Label(root, text='pictures will show in this spot', image=None) #Create a label 
l.pack() #The executor of the label

def openpicture():
	global img 
	filename = filedialog.askopenfilename() #Obtain the compleate rout 
	img = ImageTk.PhotoImage(Image.open(filename)) #tkinter only can open gif files, here I used the libary PIL 
	#Open the file in jpg Format
	l.config(image = img) #I used the method of config to put the image in th label

b = tk.Button(root, text='select a picture', command=openpicture) #I configure the boton and the command open picture
b.pack() 

tk.mainloop()
