from tkinter import *
import random

# counter = 0
# app = Tk()
# app.geometry("500x500")
# app.title("window")
# app["bg"] = "#0eb3b8"
# app.resizable(False,False)
# def name():
#     global counter
#     counter += 1
#     print(counter)
#     button["state"] = "disabled"
# button = Button(text="1 button",command=name,width=50,height=20)
#
# button.place(x = 23,y = 43)
# app.mainloop()

# app = Tk()
# app.geometry("300x300")
#
# def changer():
#     choice = random.randint(0, 255)
#     choice1 = random.randint(0, 255)
#     choice2 = random.randint(0, 255)
#     print(f"#{choice:02x}{choice1:02x}{choice2:02x}")
#     app["bg"] = (f"#{choice:02x}{choice1:02x}{choice2:02x}")
#
#
# button = Button(text="changer",command=changer,padx = 40,pady=23,bg="red",fg="blue",font=("arial",23,"regular"))
# button.place(x = 25,y = 30)
#
# app.mainloop()

app = Tk()
app.geometry('300x500+500+100')
app.title("calculator")

counter = 0
def count():
    global counter
    counter += 1
    print(counter)
    label["text"] = f"button is pushed {counter}"
    label["bg"] = "green"

    if counter == 10:
        button["state"] = "disabled"
        label["bg"] = "yellow"


button = Button(text="changer",command=count,padx = 20,pady=3,bg="red",fg="blue",font=("arial",23))

button.place(x = 25,y = 30)
label = Label(text="i have github",bg="blue",font=("arial",23))
label.place(x = 25,y = 140)
app.mainloop()

