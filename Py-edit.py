#! /usr/bin/python
#This program was written by Ben J (PythonCow).

#Tkinter is a GUI module for python that will be used for graphics.
import Tkinter as tk
from ScrolledText import ScrolledText

master = tk.Tk()
master.wm_title("Py-edit")

optionsframe = tk.Frame(master)#Create a frame above text box for options.
optionsframe.pack(pady = 5, padx = 5, side = tk.TOP)

entry = tk.Entry(optionsframe)#Entry box for opening path in top frame
entry.pack( pady = 30, side = tk.LEFT)

#Function to retrieve data from entry box and open file in textbox.
def opentext():
    global filepath
    filepath = entry.get()
   
    import os.path
    
    if os.path.exists(filepath):
        filecontents = open(filepath, 'r')
        filetext = filecontents.read()
        textbox.insert('1.0', filetext)

openbutton = tk.Button(optionsframe, text = "Open", width = 10, command = opentext )#Button to call opentext function.
openbutton.pack(padx = 5, pady = 5, side = tk.LEFT)

#Function to write data to original file.
def savefile():
    oldfile = open(filepath, 'w')
    oldfile.write(textbox.get('1.0', 'end'))
    
savebutton = tk.Button(optionsframe, text = "Save", width = 10, command = savefile )
savebutton.pack(padx = 5, pady = 5, side = tk.LEFT)

#Function to write data to new path of choice.
def saveas():
    savepath = entry2.get()
    savefile = open(savepath, 'w')
    savefile.write(textbox.get('1.0','end'))

saveasbutton = tk.Button(optionsframe, text = "Save As:", width = 10, command = saveas )#Button to call saveas function.
saveasbutton.pack(padx = 5, pady = 5, side = tk.LEFT)

entry2 = tk.Entry(optionsframe)#Entry box for new path.
entry2.pack( pady = 30, side = tk.LEFT)

textbox = ScrolledText(master)#Scrolling text box.
textbox.pack(padx = 5, pady = 5, fill = 'both', expand = 'yes')

master.mainloop()








