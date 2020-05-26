import tkinter as tk
#import motorController

xpos = 0
ypos = 0
def update_position(e):
    xpos = e.x
    ypos = e.y
    canvas.coords(xline, 0, e.y, 1024, e.y)
    canvas.coords(yline, e.x, 0, e.x, 1024)
    canvas.coords(circle, e.x-10, e.y-10, e.x+10, e.y+10)
    canvas.itemconfig(xposText, text='xposition: ' + str(xpos))
    canvas.itemconfig(yposText, text='yposition: ' + str(ypos))
    #motorController.gotoPos(xpos, ypos)

canvas = tk.Canvas(width=1024, height=1024, background='black')
canvas.pack()
#motorController.home()
xline = canvas.create_line(0,0,0,0, fill='red')
yline = canvas.create_line(0,0,0,0, fill='red')
circle = canvas.create_oval(0,0,0,0, fill='blue')
xposText = canvas.create_text(40,10, fill='white', text=('xposition: ' + str(xpos)));
yposText = canvas.create_text(40,30, fill='white', text=('yposition: ' + str(ypos)))


canvas.bind('<Motion>', update_position)

canvas.mainloop()