from tkinter import * 
from tkinter.ttk import *
from time import strftime 
#this program is all about the making digital clock using python 
root = Tk() 
root.title('Digital Clock') 
  
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  

lbl = Label(root, font = ('italic', 42, 'bold'), 
            background = 'white', 
            foreground = 'red') 
  
#hello it is digital clock 
lbl.pack(anchor = 'center') 
time() 
  
mainloop()
