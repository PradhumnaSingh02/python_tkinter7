#create widget in python
from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# the create_line command line contains a point x1, y1 and x2 , y2

can_widget.create_line(0, 0, 800, 400, fill='red')
can_widget.create_line(0, 400, 800, 0, fill='blue')
can_widget.create_rectangle(3, 5, 800, 400, fill="Yellow" )
can_widget.create_text(200, 200, text='GUI', font='Bolt')
can_widget.create_oval(200, 344, 345, 256)
root.mainloop()