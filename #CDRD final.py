#CDRD final

#this project will entaill a bunch of third party hacking options such as 
#creraating a fake phone number
#createing false creit cards
#givbing a detailed description and all info of a person online
#etc etc....

#----------------------------

#imports
import tkinter as tk
import time
import os
import math

#starup menu
'''

 ▄████▄  ▓█████▄  ██▀███  ▓█████▄ 
▒██▀ ▀█  ▒██▀ ██▌▓██ ▒ ██▒▒██▀ ██▌
▒▓█    ▄ ░██   █▌▓██ ░▄█ ▒░██   █▌
▒▓▓▄ ▄██▒░▓█▄   ▌▒██▀▀█▄  ░▓█▄   ▌
▒ ▓███▀ ░░▒████▓ ░██▓ ▒██▒░▒████▓ 
░ ░▒ ▒  ░ ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
  ░  ▒    ░ ▒  ▒   ░▒ ░ ▒░ ░ ▒  ▒ 
░         ░ ░  ░   ░░   ░  ░ ░  ░ 
░ ░         ░       ░        ░    
░         ░                ░      

Welcome to /CODE RED/ MR.CYBERS First toolkit

The tool that contains a whole bunch of other peolples tools
'''

cwd = os.getcwd()

#tinker setup
main = tk.Tk()

#this keeps events in check, its an event handler

def cwd1(event):
    print(cwd)
def listdir(event):
    os.listdir()

main.rowconfigure(0, minsize=50)
main.columnconfigure([0, 1, 2, 3], minsize=50)

button1 = tk.Button(text="CWD")
button2 = tk.Button(text="LISTDIR")


#labels
lable1 = tk.Label(
    text = "test1",
    height=20,
    width=40,
    bg="black",
    fg="white"

)

lable2 = tk.Label(
    text = "this is some MORE text",
    height=20,
    width=40,
    bg="white",
    fg="black"

)


#binding lets buttons do functions
button1.bind("<ButtonRelease-1>", cwd1)
button2.bind("<ButtonRelease-1>", listdir)


#you have to pack each element to use it 
button1.grid(row=0,column=0)
button2.grid(row=0,column=1,rowspan=2,columnspan=2)
lable1.grid(row=2,column=0)
lable2.grid(row=2,column=1)



main.mainloop() #any code after this will not run until tk window is closed 


