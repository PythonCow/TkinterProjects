#This program was written by Ben Jamison.

#Tkinter is a GUI module for python that will be used for graphics.
import Tkinter as tk


#Requests user input.

input_master = tk.Tk()

tk.Label(input_master, text = "f(x) = ").pack(side = tk.LEFT, padx = 10)

entry = tk.Entry(input_master)
entry.pack( pady = 30, side = tk.LEFT)
entry.focus_set()

def enterget():
    global function
    function = entry.get()
    input_master.destroy()
    
    
btn = tk.Button(input_master, text = "OK",width = 10, command = enterget)
btn.pack(side = tk.RIGHT, padx = 10)

input_master.mainloop()

#Set up the canvas widget.
master = tk.Tk()
graph = tk.Canvas(master, width = 1000, height = 1000)
graph.pack(pady = 10, padx = 10)
#Create x and y axies.
graph.create_rectangle(0,0,1000,1000, fill = "white")
graph.create_line(0,500,1000,500)
graph.create_line(500,0,500,1000)

#Draws a marker every 10 pixels for reference.
xcoord = 0
while xcoord < 1001:
    xcoord += 10
    graph.create_rectangle(xcoord,500,xcoord,501)
ycoord = 0
while ycoord < 1001:
    ycoord += 10
    graph.create_rectangle(500,ycoord,501,ycoord)

#Puts the user input into a function.
output =  lambda x: eval(function)
xpoints = range(0,1500)#List of points on the x axis.
ypoints = []#List of points on the y axis. Will be determined by user input.
graphypoints = []#Same list as above, but adapted to be used by the Canvas widget.
#This loop runs 1000 different inputs through the function and puts the output in the ypoints and graphypoints lists.
inpt = float(-100.0000)
while inpt<101:
    ypoint =  output(inpt)
    inpt+=0.1
    ypoints.append(ypoint)
    graphypoints.append((ypoint*10))

count = 0
#graphypoints needs to be changed so it will be graphed correctly.
while count< len(graphypoints) :
    graphypoints[count] =  (-graphypoints[count])+500
    count+= 1

#The next little block of code looks for '**' and '-' in the user input to know what kind of function it is.
len_func = len(function)
exponent = False
negative = False
count = 0 
while count < (len_func ):
    if exponent == True:
        func_exponent = function[count]
        break
    elif function[count] == "*":
        if function[count +1] == "*":
            exponent = True
            count += 1
    elif function[count] == "-" :
        negative = True
    count += 1

#This codes determines the multiplicity, maximum turning points, and end behavior based on variables set by the previous loop.
if exponent == True :
    
    graph.create_text(900,25, text = "Multiplicity: "+str(func_exponent))#Writes multiplicity on Canvas.
    graph.create_text(900,40, text = "Max Turning Points: " +str(int(func_exponent) - 1))#Writes max turning points on the Canvas.
    if negative == False :#Functions have different end behvior if they are negative.
        if int(func_exponent)%2 == 0:#Functions have different end behavior if the largest exponent is even.
            end_behavior = "as x -> infinity, f(x) -> infinity \n as x -> -infinity, f(x) -> infinity"
        else :
            end_behavior = "as x -> infinity, f(x) -> infinity \n as x -> -infinity, f(x) -> -infinity"
    else:#Functions that are negative have opposite end behavior.
        if int(func_exponent)%2 == 0:
            end_behavior = "as x -> infinity, f(x) -> -infinity \n as x -> -infinity, f(x) -> -infinity"
        else :
            end_behavior = "as x -> infinity, f(x) -> -infinity \n as x -> -infinity, f(x) -> infinity"
else:#If functions do not have an exponent, they act like a function with an odd exponent.
    if negative == False:
        end_behavior = "as x -> infinity, f(x) -> infinity \n as x -> -infinity, f(x) -> -infinity"
    else :
        end_behavior = "as x -> infinity, f(x) -> -infinity \n as x -> -infinity, f(x) -> infinity"

graph.create_text(900,60, text = end_behavior)#Writes End  behavior on the Canvas.
#Finally, the program graphs the function.
point = 0
while point < len(xpoints)- 1:#Instead of graphing each individual point, a line from each point to the next is drawn, eliminating any gaps.
    graph.create_rectangle(xpoints[point]-500, (graphypoints[int(point)]), xpoints[int(point)+1]-500,(graphypoints[int(point)+ 1]), fill = "black", activefill = "blue")
    point+= 1

master.mainloop()

