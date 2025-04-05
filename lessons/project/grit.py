from tkinter import *

app = Tk()
app.geometry('700x700')
mypadx = 80
mypady = 80


def info(number):
    print(number)

num = [1,2,3,4,5,6,7,8,9]
b=0
r = 0
c = 0
for i in range(3):
    for j in range (3):
        button = Button(command= lambda b=b:info(number=b),padx=mypadx,pady=mypady,bg="#daf7a6")
        button.grid(row=r,column=c+j)
        b+=1

    r+=1




# button1 = Button(padx=mypadx,pady=mypady)
# button1.grid(row=1,column=1,padx=mypadx,pady=mypady,sticky="nsew")
# button2 = Button(padx=mypadx,pady=mypady)
# button2.grid(row=2,column=1,sticky="nsew",padx=mypadx,pady=mypady)
# button3 = Button(padx=mypadx,pady=mypady)
# button3.grid(row=3,column=1,padx=mypadx,pady=mypady,sticky="nsew")
# button4 = Button(padx=mypadx,pady=mypady)
# button4.grid(row=1,column=2,padx=mypadx,pady=mypady,sticky="nsew")
# button5 = Button(padx=mypadx,pady=mypady)
# button5.grid(row=2,column=2,sticky="nsew",padx=mypadx,pady=mypady)
# button6 = Button(padx=mypadx,pady=mypady)
# button6.grid(row=2,column=3,sticky="nsew",padx=mypadx,pady=mypady)
# button7 = Button(padx=mypadx,pady=mypady)
# button7.grid(row=1,column=3,padx=mypadx,pady=mypady,sticky="nsew")
# button8 = Button(padx=mypadx,pady=mypady)
# button8.grid(row=3,column=2,sticky="nsew",padx=mypadx,pady=mypady)
# button9 = Button(padx=mypadx,pady=mypady)
# button9.grid(row=3,column=3,sticky="nsew",padx=mypadx,pady=mypady)
for col in range(4):
    app.grid_columnconfigure(col, weight=1)

for row in range(5):
    app.grid_rowconfigure(row, weight=1)



app.mainloop()