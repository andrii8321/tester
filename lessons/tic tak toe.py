import tkinter.messagebox
from tkinter import *

from PIL import Image, ImageTk

app = Tk()
app.geometry('700x700')

color= "#535353"

nul = [0,0,0,0,0,0,0,0,0]
occ = []
xon = 1
def begin(event):
    global nul
    global occ
    global xon
    button["bg"] = color
    button1["bg"] = color
    button2["bg"] = color
    button3["bg"] = color
    button4["bg"] = color
    button5["bg"] = color
    button6["bg"] = color
    button7["bg"] = color
    button8["bg"] = color
    nul = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    occ = []
    xon = 1

def click(button,num):
    global occ,nul,xon
    if not num in occ:
        if xon == 1:
            button["bg"] = "#c10808"
            image = Image.open("cross.png")
            image = image.resize((button.winfo_width(), button.winfo_height()))
            photo = ImageTk.PhotoImage(image)
            button.config(image=photo, text="", compound="center")
            nul[num] = xon
            xon = 2
        elif xon == 2:
            button["bg"] = "#00ffbd"
            nul[num] = xon
            xon = 1
    occ.append(num)

    winner()



mypadx = 80
mypady = 80

def winner():
    end = False
    if nul[0]==nul[1]==nul[2]>0:
        winner = nul[1]
        end=True
    elif nul[3]==nul[4]==nul[5]>0:
        winner = nul[3]
        end = True
    elif nul[6]==nul[7]==nul[8]>0:
        winner = nul[6]
        end = True
    elif nul[0]==nul[3]==nul[6]>0:
        winner = nul[3]
        end = True
    elif nul[1]==nul[4]==nul[7]>0:
        end = True
        winner = nul[7]
    elif nul[2]==nul[5]==nul[8]>0:
        end = True
        winner =  nul[4]
    elif nul[0]==nul[4]==nul[8]>0:
        end = True
        winner =  nul[4]
    elif nul[2]==nul[4]==nul[6]>0:
        end = True
        winner =  nul[4]
    elif len(occ) == 9   :
        tkinter.messagebox.showinfo("End of the game","Draw")
        begin(None)
    if end==True:
        if winner == 1:
            tkinter.messagebox.showinfo("End of the game", "Winner is cross")
        elif winner == 2:
            tkinter.messagebox.showinfo("End of the game","Winner is nulik")
        begin(None)

def info():
    tkinter.messagebox.showinfo("12","f1-дає інформацію, f12-перезапускає гру,escape-закінчує гру")

def f12(event):
    begin(event)

def escape():
    app.destroy()

button = Button(command=lambda: click(button,0),padx=mypadx,pady=mypady,bg=color)
button.place(x = 50, y = 50)

button1 = Button(command=lambda: click(button1,1),padx=mypadx,pady=mypady,bg=color)
button1.place(x = 250,y=50)

button2 = Button(command=lambda: click(button2,2),padx=mypadx,pady=mypady,bg=color)
button2.place(x = 450,y=50)

button3 = Button(command=lambda: click(button3,3),padx=mypadx,pady=mypady,bg=color)
button3.place(x = 50, y = 250)

button4 = Button(command=lambda: click(button4,4),padx=mypadx,pady=mypady,bg=color)
button4.place(x = 250, y = 250)

button5 = Button(command=lambda: click(button5,5),padx=mypadx,pady=mypady,bg=color)
button5.place(x = 450, y = 250)

button6 = Button(command=lambda: click(button6,6),padx=mypadx,pady=mypady,bg=color)
button6.place(x = 50, y = 450)

button7 = Button(command=lambda: click(button7,7),padx=mypadx,pady=mypady,bg=color)
button7.place(x = 250, y = 450)

button8 = Button(command=lambda: click(button8,8),padx=mypadx,pady=mypady,bg=color)
button8.place(x = 450, y = 450)
app.bind('<e>',lambda e: click(button,0) )
app.bind('<r>',lambda e: click(button1,1) )
app.bind('<t>',lambda e: click(button2,2) )
app.bind('<d>',lambda e: click(button3,3) )
app.bind('<f>',lambda e: click(button4,4) )
app.bind('<g>',lambda e: click(button5,5) )
app.bind('<c>',lambda e: click(button6,6) )
app.bind('<v>',lambda e: click(button7,7) )
app.bind('<b>',lambda e: click(button8,8) )
app.bind('<Escape>',lambda e :escape())
app.bind('<F12>',lambda e :f12(e))
app.bind('<F1>',lambda e :info())


app.mainloop()