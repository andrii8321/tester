from tkinter import *



# app = Tk()
# app.geometry('300x300')
#
#
# def leave():
#     app.destroy()
#
# button = Button(text="нова гра",font=('arial',24),padx=80,pady=40)
# button.place(x=0,y=0)
# button1 = Button(command=leave,text="вихід     ",font=('arial',24),padx=80,pady=40)
# button1.place(x=0,y=155)

appp =Tk()


m =0
shrift = ('arial',25)
counter = 16
after_d = None
i = 0



questions = {0:{"name":"Який континент складається лише з однієї країни?!",
                  "answers":["Європа", "Азія", "Африка", "Австралія"],"correct_answer":4},
             1:{"name":"Де ростуть соняшники?",
                "answers":["На землі", "На сонці", "На небі", "У воді"],"correct_answer":1},
             2:{"name":"Яких грошей не буває?",
                "answers":["Гривні", "Льє", "Долари", "Ліри"],"correct_answer":2},
             3:{"name":"Як називається портрет, який написаний з самого себе?",
                "answers":["Самоскит", "Самописка", "Зеркальник", "Автопортрет"],"correct_answer":4},
             4:{"name":"Як називають безпілотний літальний апарат?",
                "answers":["Дрон", "Махаон", "Десептикон", "Аніон"],"correct_answer":1},
             5:{"name":"В якій грі не використовують м’яч?",
                "answers":["Баскетбол", "Теніс", "Бейсбол", "Керлінг"],"correct_answer":4},
             6:{"name":"Який з цих мостів знаходиться в Києві?",
                "answers":["Празький", "Дарницький", "Невський", "Славутицький"],"correct_answer":2},
             7:{"name":"Хто з цих людей є письменником?",
                "answers":["Жан-Клод Вандам", "Клод Моне", "Усейн Болт", "Едгар По"],"correct_answer":4},
             8:{"name":"Хто з цих мореплавців відкрив Мис Доброї Надії?",
                "answers":["Бартоломео Діаш", "Джон Брюс", "Васка Дагама", "Христофор Колумб"],"correct_answer":1},
             }



quest = ["Який континент складається лише з однієї країни?", "Де ростуть соняшники?",
         "Яких грошей не буває?", "Як називається портрет, який написаний з самого себе?",
         "Як називають безпілотний літальний апарат?", "В якій грі не використовують м’яч?",
         "Який з цих мостів знаходиться в Києві?", "Хто з цих людей є письменником?",
         "Хто з цих мореплавців відкрив Мис Доброї Надії?"]

answer = [["Європа", "Азія", "Африка", "Австралія"], ["На землі", "На сонці", "На небі", "У воді"],
          ["Гривні", "Льє", "Долари", "Ліри"], ["Самоскит", "Самописка", "Зеркальник", "Автопортрет"],
          ["Дрон", "Махаон", "Десептикон", "Аніон"], ["Баскетбол", "Теніс", "Бейсбол", "Керлінг"],
          ["Празький", "Дарницький", "Невський", "Славутицький"], ["Жан-Клод Вандам", "Клод Моне", "Усейн Болт", "Едгар По"],
          ["Бартоломео Діаш", "Джон Брюс", "Васка Дагама", "Христофор Колумб"]]

correct_answer = [4, 1, 2, 4, 1, 4, 2, 4, 1]

def next_question(number):
    global label_question,button_ans1,button_ans2,button_ans3,button_ans4,i,counter,m
    button_ans1.config(state="normal")
    button_ans2.config(state="normal")
    button_ans3.config(state="normal")
    button_ans4.config(state="normal")
    counter = 16
    if i >= 8:
        m+=900
        appp.destroy()
        bpp = Tk()
        bpp.geometry('300x400')
        label_end  = Label(text="кінець,ви виграли",font=('arial',30))
        label_end.place(x=0,y=0)
        label_summa = Label(text=f"summa:{m}",font=('arial',30))
        label_summa.place(x=0,y=100)
    elif correct_answer[i] == number:
        i +=1

        label_question["text"] = questions[i]["name"]
        button_ans1["text"] = questions[i]["answers"][0]
        button_ans2["text"] = questions[i]["answers"][1]
        button_ans3["text"] = questions[i]["answers"][2]
        button_ans4["text"] = questions[i]["answers"][3]
        label_indikator["text"] = f"питання номер:{i+1} "
        m += i*100
        label_cash["text"] = f"сума:{m}"
    else:
        appp.destroy()
        bpp = Tk()
        bpp.geometry('500x200')
        label_end = Label(text="кінець, ви програли", font=('arial', 30))
        label_end.place(x=0, y=0)
        if i >= 5:
            m= 1500
        else:
            m=0

        label_summa = Label(text=f"summa:{m}", font=('arial', 30))
        label_summa.place(x=0, y=100)



def cashout():
    appp.destroy()
    bppp = Tk()
    bppp.geometry('500x200')
    label_end = Label(text=f"кінець, ваш баланс:{m}", font=('arial', 30))
    label_end.place(x=0, y=0)



# button.config(state="disabled")


def help():
    if correct_answer[i] == 1:
        button_ans2.config(state="disabled")
        button_ans4.config(state="disabled")
        button_ans3.config(state="disabled")
    if correct_answer[i] == 2:
        button_ans1.config(state="disabled")
        button_ans4.config(state="disabled")
        button_ans3.config(state="disabled")
    if correct_answer[i] == 3:
        button_ans2.config(state="disabled")
        button_ans4.config(state="disabled")
        button_ans1.config(state="disabled")
    if correct_answer[i] == 4:
        button_ans2.config(state="disabled")
        button_ans1.config(state="disabled")
        button_ans3.config(state="disabled")
    button_help.config(state="disabled")
def fifty_fifty():
    if correct_answer[i] == 1:
        button_ans2.config(state="disabled")
        button_ans4.config(state="disabled")
    if correct_answer[i] == 2:
        button_ans3.config(state="disabled")
        button_ans1.config(state="disabled")
    if correct_answer[i] == 3:
        button_ans4.config(state="disabled")
        button_ans1.config(state="disabled")
    if correct_answer[i] == 4:
        button_ans3.config(state="disabled")
        button_ans1.config(state="disabled")
    button_fifty_fifty.config(state="disabled")

appp.geometry('900x700')
label_timer = Label(text="таймер",font=shrift)
label_timer.place(x=250,y=0)
label_cash =Label(text=f"сума:{i*100}",font=shrift)
label_cash.place(x=650,y=0)
button_help = Button(command=help,text="допомога",font=shrift)
button_help.place(x=50,y=140)
button_fifty_fifty = Button(command=fifty_fifty,text="50/50",font=shrift)
button_fifty_fifty.place(x=350,y=140)
button_cashback = Button(command=cashout,text="забрати гроші",font=shrift)
button_cashback.place(x=650,y=140)
label_indikator = Label(text=f"питання номер:{i+1} ",font=('arial',17))
label_indikator.place(x=0,y=340)
label_question = Label(text=questions[i]["name"],font=shrift)
label_question.place(x=0,y=380)
button_ans1 = Button(text = questions[i]["answers"][0]                        ,command=lambda: next_question(number=1),font=shrift)
button_ans1.place(x=50,y=440)
button_ans2 = Button(text=questions[i]["answers"][1]                        ,command=lambda:next_question(number=2),font=shrift)
button_ans2.place(x=470,y=440)
button_ans3 = Button(text=questions[i]["answers"][2]                        ,command=lambda:next_question(number=3),font=shrift)
button_ans3.place(x=50,y=540)
button_ans4 = Button(text=questions[i]["answers"][3]                        ,command=lambda:next_question(number=4),font=shrift)
button_ans4.place(x=470,y=540)

def timer():
    global label_timer, counter,after_d,m
    after_d = label_timer.after(1000,timer)
    counter -= 1
    label_timer["text"] = counter
    if counter <= 0:
        appp.destroy()
        bppp = Tk()
        bppp.geometry('500x200')
        label_end = Label(text="кінець, час вичерпано", font=('arial', 30))
        label_end.place(x=0, y=0)

        if i >= 5:
            m= 1500
        else:
            m=0
        label_summa = Label(text=f"summa:{m}", font=('arial', 30))
        label_summa.place(x=0, y=100)


timer()








appp.mainloop()