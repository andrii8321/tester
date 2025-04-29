from tkinter import *
import random
import tkinter.messagebox
can = Tk()
can.title("Полотно для малювання")
can.geometry()
can.resizable (False, False)
cant = Canvas(width=1000, height=500, bg='white')
cant.pack()


x = 5
y = -5
bolt_y = 180
bolt_x = 230

count = 0
count1 = 0
color = "white"
cant.create_rectangle(0,0,1000,500,fill="green")
cant.create_line(500,0,500,500,width=5,fill=color)
text1 = cant.create_text(200,40,text=count1,font='Arial 50')
text2 = cant.create_text(800,40,text=count,font='Arial 50')
ball1 = cant.create_oval(bolt_x,bolt_y,bolt_x+30,bolt_y+30,fill=color)
plat1 = cant.create_rectangle(20,250,30,330,fill=color)
plat2 = cant.create_rectangle(970,250,980,330,fill=color)

def moving(event):

    if cant.coords(plat1)[1] - 20 > 0 and event.keysym == "w":
        cant.move(plat1, 0, -20)
    elif cant.coords(plat1)[3] + 20 < 500 and event.keysym == "s":
        cant.move(plat1, 0, 20)
    elif cant.coords(plat2)[1] - 20 >  0 and event.keysym == "Up":
        cant.move(plat2, 0, -20)
    elif cant.coords(plat2)[3] + 20 < 500 and event.keysym == "Down":
        cant.move(plat2, 0, 20)




def ball():
    global ball1,bolt_y,bolt_x,x,y,count,count1,text1,text2
    cant.move(ball1,x,y)
    cant.after(10, ball)
    bolt_x+=x
    bolt_y+=y
    if bolt_y+y> 480:
        y = -y
    elif bolt_y+y < 0:
        y = -y
    elif bolt_x+x+10 >980:
        cant.delete(text1)
        count1 += 1
        text1 = cant.create_text(200, 40, text=count1, font='Arial 50')

        x = -x
    elif bolt_x <0:
        cant.delete(text2)
        count += 1
        text2 = cant.create_text(800, 40, text=count, font='Arial 50')
        x = -x
    if (cant.coords(ball1)[2] > cant.coords(plat2)[0] and
            cant.coords(ball1)[2] < cant.coords(plat2)[2] and
            cant.coords(ball1)[1] > cant.coords(plat2)[1] and
            cant.coords(ball1)[1] < cant.coords(plat2)[3]):
        # x =random.randint(4,6)*-1
        # y = random.randint(4,6)
        x = -x
        y = -y
    elif (cant.coords(ball1)[0] < cant.coords(plat1)[2] and
             cant.coords(ball1)[0] > cant.coords(plat1)[0] and
             cant.coords(ball1)[1] > cant.coords(plat1)[1]and
             cant.coords(ball1)[1] < cant.coords(plat1)[3]):
        # x = random.randint(4,6)
        # y = random.randint(4, 6)
        x = -x
        y = yd
    win()

def win():
    if count-count1 >= 2 and count >= 11:
        can.destroy()
        tkinter.messagebox.showinfo("win",'first player won')
    elif  count1-count>=2 and count1>=11:
        can.destroy()
        tkinter.messagebox.showinfo("win", 'second player won')



ball()




cant.focus_set()
cant.bind('<w>', moving)
cant.bind('<s>', moving)
cant.bind('<Up>', moving)
cant.bind('<Down>', moving)
cant.mainloop()