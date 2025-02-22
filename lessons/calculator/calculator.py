from tkinter import *


lblx = 0
lbly = 0
nul = 0
zeronul = 0
num = 0
num2 = 0
znak = "n"



def q(number):
    global nul
    global zeronul
    global num
    global num2
    global lblx
    global lbly
    if nul == 0:
        nul = 1
        lbl["text"] = str(number)
    else:
        lbl["text"] += str(number)
    if zeronul == 0:
        lblx = int(lbl["text"])
    else:
        lbly = int(lbl["text"])
def q2():
    q(2)
def q3():
    q(3)
def q1():
    q(1)
def q4():
    q(4)
def q5():
    q(5)
def q6():
    q(6)
def q7():
    q(7)
def q8():
    q(8)
def q9():
    q(9)
def q0():
    q(0)
def q_clear():
    lbl["text"]= ""
def btnznak(z):
    global nul
    global zeronul
    global znak
    global lblx
    global lbly
    lbl["text"] = lbl["text"] + z
    nul = 0
    zeronul = 1
    znak = z
def btpl():
    btnznak("+")
def btmin():
    btnznak("-")
def btmn():
    btnznak("*")
def btdel():
    btnznak("/")

def eq():
    global lblx, lbly,znak,zeronul,nul
    if znak == "+":
        lbl["text"] = f"{lblx+lbly}"
    elif znak == "-":
        lbl["text"] = f"{lblx-lbly}"
    elif znak == "*":
        lbl["text"] = f"{lblx*lbly}"
    else:
        try:
            lbl["text"] = f"{lblx / lbly}"
        except ZeroDivisionError:
            lbl["text"] = "you cant devide on zero"
    lblx = float(lbl["text"])
    lbly = 0
    nul = 0
    zeronul = 0
app = Tk()
app.geometry('600x600')
app.title("calculator")
app["bg"] = "#d1ae01"

color = "#0970b8"
mypadx = 35
mypady = 28

lbl = Label(padx=15,width=40,pady=30, bg="grey",font=("arial",24))
lbl.place(x = 0, y = 0)


button1 = Button(command=q2,text="2",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button1.place(x = 170,y = 110)

button2 = Button(command=q3,text="3",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button2.place(x = 290, y = 110)

button3 = Button(command=q4,text="4",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button3.place(x = 50,y = 220)

button4 = Button(command=q5,text="5",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button4.place(x = 170,y = 220)

button5 = Button(command=q6,text="6",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button5.place(x = 290, y = 220)

button6 = Button(command=q7,text="7",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button6.place(x = 50,y = 330)

button7 = Button(command=q8,text="8",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button7.place(x = 170,y = 330)

button8 = Button(command=q9,text="9",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button8.place(x = 290,y = 330)

button1 = Button(command=q1,text="1",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button1.place(x = 50,y = 110)

button_clear = Button( command=q_clear,text="AC",pady=mypady,padx=mypadx-10,font=("arial",18),bg=color)
button_clear.place(x = 50,y = 440)

button_equals = Button(command=eq,text="=",pady=mypady,padx=mypadx,font=("arial",18),bg=color)
button_equals.place(x = 290,y = 440)

button_minus = Button(command=btmin,text="-",pady=mypady,padx=mypadx,font=("arial",18),bg=color)
button_minus.place(x = 410,y = 110)

button_plus = Button(command=btpl,text="+",padx=mypadx-3,pady=mypady,font=("arial",18),bg=color)
button_plus.place(x = 410,y = 220)

button_multi = Button(command=btmn,text="*",padx=mypadx-1,pady=mypady,font=("arial",18),bg=color)
button_multi.place(x = 410,y = 330)

button_devide = Button(command=btdel,text="/",padx=mypadx,pady=mypady,font=("arial",18),bg=color)
button_devide.place(x = 410,y = 440)

button_zero = Button(command=q0,text="0",pady=mypady,padx=mypadx,font=("arial",18),bg=color)
button_zero.place(x = 170,y = 440)




app.mainloop()
