from tkinter import *
import random

choose = ["paper","scisor","rock"]
choice = ""


def my_choice(text):
    print("my choice:",text)
    c = random.choice(choose)
    check(my_choice = text,comp_choice = c )



def check(my_choice,comp_choice):
    print("computer:",comp_choice)
    label_comp["text"] = f'{v}:{comp_choice}'
    if my_choice == "scisor":
        if comp_choice == "rock":
            print("computer win")
        elif comp_choice == "paper":
            print("you win")
        elif comp_choice == "scisor":
            print("draw")
    elif my_choice == "rock":
        if comp_choice == "paper":
            print("computer win")
        elif comp_choice == "scisor":
            print("you win")
        elif comp_choice == "rock":
            print("draw")
    elif my_choice == "paper":
        if comp_choice == "scisor":
            print("computer win")
        elif comp_choice == "paper":
            print("draw")
        elif comp_choice == "rock":
            print("you win")




v = "computer choice"

mypadx = "50"
mypady = "25"
app =  Tk()
app.geometry('500x500')

label_winner = Label(text="label",padx="20",pady="30",font=("arial",30))
label_winner.place(x=30,y=0)

label_comp = Label(text = v,padx="20",pady="30",font=("arial",30))
label_comp.place(x = 30,y = 30)

button_paper = Button(command=lambda:my_choice("paper"),text="paper",padx=mypadx,pady=mypady)
button_paper.place(x = 50,y = 400)

button_scisor = Button(command=lambda:my_choice("scisor"),text="scisor",pady=mypady,padx=mypadx)
button_scisor.place(x = 190, y = 400)

button_rock = Button(command= lambda:my_choice("rock"),text="rock",padx=mypadx,pady=mypady)
button_rock.place(x = 330,y = 400)
app.mainloop()


