from tkinter import *
can = Tk()
can.title("Полотно для малювання")
can.geometry()
can.resizable (False, False)
cant = Canvas(width=500, height=500, bg='white')
cant.pack()

# cant.create_oval(0, 0, 490, 490,
# fill='yellow', outline='black')
# cant.create_line(100,300,180,350,fill='red',width=5)
# cant.create_line(300,350,380,300,fill='red',width=5)
# cant.create_line(180,350,300,350,fill='red',width=5)
# cant.create_arc(100, 100, 190, 190,
# start=0, extent=180,
# fill='black')
# cant.create_arc(300,100, 390, 190,
# start=0, extent=180,
# fill='black')


cant.create_rectangle(100,180,340,390,fill="grey")
cant.create_rectangle(140,220,300,350,fill="green")
cant.create_rectangle(180,260,260,310,fill="yellow")
cant.create_line(100, 180, 140, 220, fill='green',width=5)
cant.create_line(300, 220, 340, 180, fill='green',width=5)
cant.create_line(100, 390, 140, 350, fill='green',width=5)
cant.create_line(300, 350, 340, 390, fill='green',width=5)



# cant.create_line(100, 180, 100, 60, fill='green',
# width=5, arrow=LAST, dash=(10,2),
# activefill='lightgreen',
# arrowshape="10 20 10")
# cant.create_rectangle(60, 80, 140, 190,
# fill='yellow',
# outline='green',
# width=3,
# activedash=(5, 4))
# cant.create_rectangle(50, 10, 150, 110,outline="red")
# cant.create_oval(50, 10, 150, 110, width=2)
# cant.create_oval(10, 120, 190, 190,
# fill='grey70', outline='white')
# cant.create_oval(10, 10, 290, 290,
# fill='lightgrey',
# outline='white')
# cant.create_arc(10, 10, 190, 190,
# start=0, extent=45,
# fill='red')
# cant.create_arc(10, 10, 190, 190,
# start=180, extent=25, fill='orange')
# cant.create_arc(10, 10, 190, 190,
# start=240, extent=100,
# style=CHORD, fill='green')
# cant.create_arc(10, 10, 190, 190,
# start=160, extent=-70,
# style=ARC, outline='darkblue',
# width=5)
# cant.create_text(100, 100,
# text="Hello World,\nPython\nand Tk",
# justify=CENTER, font="Verdana 14")
can.mainloop()