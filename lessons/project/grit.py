
from tkinter import *

app = Tk()
app.geometry('500x550')
mypadx = 80
mypady = 80
spisok =[0,0,0,0,0,0,0,0,0]
list = []
tumbler1 = 1

def ch(button,number):
    global tumbler1
    if number not in list:
        spisok[number - 1] = tumbler1
        if tumbler1 == 1:
            color = "#ad0707"
            tumbler1 = 2
        elif tumbler1 == 2:
            color = "#0b6a8e"
            tumbler1 = 1
        
        button["bg"]=color
        list.append(number)
    winner()
def winner():
    global spisok,winner
    if spisok[0]==spisok[3]==spisok[6] and spisok[0]!=0:
        winner = spisok[0]
    elif spisok[0]==spisok[1]==spisok[2] and spisok[0]!=0:
        winner = spisok[0]
    elif spisok[0] == spisok[4] == spisok[8] and spisok[0]!=0:
        winner = spisok[0]
    elif spisok[0]==spisok[1]==spisok[2] and spisok[0]!=0:
        winner = spisok[0]
    elif spisok[1]==spisok[4]==spisok[7] and spisok[1]!=0:
        winner = spisok[1]
    elif spisok[2]==spisok[5]==spisok[8] and spisok[2]!=0:
        winner = spisok[2]
    elif spisok[2]==spisok[4]==spisok[6] and spisok[2]!=0:
        winner = spisok[2]
    elif spisok[3]==spisok[4]==spisok[5] and spisok[3]!=0:
        winner = spisok[3]
    elif spisok[6]==spisok[7]==spisok[8] and spisok[7]!=0:
        winner = spisok[7]
    elif len(list)==9:
        print("draw")

    if winner == 1:
        print("winner X")
    elif winner == 2:
        print("winner O")



button1 = Button(command=lambda:ch(button=button1,number=1),padx=mypadx,pady=mypady)
button1.grid(row=0,column=0)
button2 = Button(command=lambda:ch(button=button2,number=2),padx=mypadx,pady=mypady)
button2.grid(row=0,column=1)
button3 = Button(command=lambda:ch(button=button3,number=3),padx=mypadx,pady=mypady)
button3.grid(row=0,column=2)
button4 = Button(command=lambda:ch(button=button4,number=4),padx=mypadx,pady=mypady)
button4.grid(row=1,column=0)
button5 = Button(command=lambda:ch(button=button5,number=5),padx=mypadx,pady=mypady)
button5.grid(row=1,column=1)
button6 = Button(command=lambda:ch(button=button6,number=6),padx=mypadx,pady=mypady)
button6.grid(row=1,column=2)
button7 = Button(command=lambda:ch(button=button7,number=7),padx=mypadx,pady=mypady)
button7.grid(row=2,column=0)
button8 = Button(command=lambda:ch(button=button8,number=8),padx=mypadx,pady=mypady)
button8.grid(row=2,column=1)
button9 = Button(command=lambda:ch(button=button9,number=9),padx=mypadx,pady=mypady)
button9.grid(row=2,column=2)


app.mainloop()