from tkinter import *
import random

choose = ["paper","scisor","rock"]
choice = ""


def my_choice(text):
    print("my choice:",text)
    c = random.choice(choose)
    check(my_choice = text,comp_choice = c )
class Result:
    win = "😉 you win"
    draw='draw'
    lose="computer win"


def check(my_choice,comp_choice):
    print("computer:",comp_choice)
    label_comp["text"] = f'{v}:{comp_choice}'
    if my_choice == "scissor":
        if comp_choice == "rock":
            label_winner["text"]="computer win"
        elif comp_choice == "paper":
            label_winner["text"] =Result.win
        elif comp_choice == "scisor":
            label_winner["text"] = 'draw'
    elif my_choice == "rock":
        if comp_choice == "paper":
            label_winner["text"] ='computer win'
        elif comp_choice == "scisor":
            label_winner["text"] =Result.win
        elif comp_choice == "rock":
            label_winner["text"] ='draw'
    elif my_choice == "paper":
        if comp_choice == "scisor":
            label_winner["text"] ='computer win'
        elif comp_choice == "paper":
            label_winner["text"] ='draw'
        elif comp_choice == "rock":
            label_winner["text"] =Result.win
    change_color(label_winner)
def change_color(label):
    if label["text"] == "computer win":
        label["bg"]="#ff0000"
    elif label["text"] == "draw":
        label["bg"] = "#f3ff00"
    else:
        label["bg"] = "#5dff00"
font = ("arial",24)
color = "#00b5f9"

v = "computer choice"

mypadx = "50"
mypady = "25"
app =  Tk()
app.geometry('630x600')
app["bg"]="#aa00ff"

label_winner = Label(text="",padx="20",pady="30",font=("arial",30),bg="#aa00ff")
label_winner.place(x=120,y=180)

label_comp = Label(text = v,padx="20",pady="30",font=("arial",30),bg="#aa00ff")
label_comp.place(x = 30,y = 30)

button_paper = Button(command=lambda:my_choice("paper"),text="paper",padx=mypadx,pady=mypady,bg=color,font=font)
button_paper.place(x = 0,y = 400)

button_scisor = Button(command=lambda:my_choice("scisor"),text="scisor",pady=mypady,padx=mypadx,bg=color,font=font)
button_scisor.place(x = 215, y = 400)

button_rock = Button(command= lambda:my_choice("rock"),text="rock",padx=mypadx,pady=mypady,bg=color,font=font)
button_rock.place(x = 430,y = 400)
app.mainloop()


