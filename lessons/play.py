from collections import defaultdict
from tkinter import *
import random

app = Tk()
app.geometry("500x500")

color = "#f80000"
instrument = ["scisor","paper","rock"]

def comp_choice(choice):
    des = random.randrange(0,len(instrument))
    label_comp["text"] = f"computer choice:{instrument[des]}"

    if choice == 'scisor':
        if des == 0:
            label_winner["text"] = "winner:draw"
        elif des == 1:
            label_winner["text"] = "winner:you"
        else:
            label_winner["text"] = "winner:computer"
    elif choice == 'rock':
        if des == 0:
            label_winner["text"] = "winner:you"
        elif des == 1:
            label_winner["text"] = "winner:computer"
        else:
            label_winner["text"] = "winner:draw"
    elif choice == 'paper':
        if des == 0:
            label_winner["text"] = "winner:computer"
        elif des == 1:
            label_winner["text"] = "winner:draw"
        else:
            label_winner["text"] = "winner:you"



def scisor():
    comp_choice('scisor')
    button_scisor["bg"]= color
    
def paper():
    comp_choice('paper')
    button_paper["bg"]= color
def rock():
    comp_choice('rock')
    button_rock["bg"]= color

shrift = "arial 24"
x = 50
y = 50
button_scisor = Button(command=scisor,text='SCISOR',pady=y,padx=x)
button_scisor.place(x = 0,y = 0)
button_rock = Button(command=rock,text='ROCK',padx=x,pady=y)
button_rock.place(x=155,y=0)
button_paper = Button(command=paper,text="PAPER",pady=y,padx=x)
button_paper.place(x=300,y=0)
label_winner = Label(text="winner:",padx=x,pady=y,font=shrift)
label_winner.place(x = 0,y = 250)
label_comp = Label(text="computer choice:",font=shrift)
label_comp.place(x = 50,y = 200)
app.mainloop()