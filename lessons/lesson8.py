
def start(name):
    print("\t\t\t\t***************")
    print(f"\t\t\t\t*Привіт, {name}!*")
    print("\t\t\t\t*Начинаем игру*")
    print("\t\t\t\t***************")


def player_info(name, pidkazka50, pidkazkaDzvonok, n_summa, summa):
    print("\t\t\t\t***************")
    print(f"\t\t\t\t* Ім'я: {name} *")
    print(f"\t\t\t\t* Використані підказки:")
    if pidkazka50:
        print(f"\t\t\t\t* 50/50: Доступна *")
    else:
        print(f"\t\t\t\t* 50/50: Не Доступна *")
    if pidkazkaDzvonok:
        print(f"\t\t\t\t* 50/50: Доступна *")
    else:
        print(f"\t\t\t\t* 50/50: Не Доступна *")
    print(f"\t\t\t\t* Незгораєма сума грошей: {n_summa} *")
    print(f"\t\t\t\t* Сума виграшу на даний момент: {summa} *")
    print("\t\t\t\t***************")


def dost_podskazki(summa, pidkazka50, pidkazkaDzvonok):
    print(f"\t\t\t\tСума виграшу на даний момент: {summa}")
    print("\t\t\t\tДоступні підказки:")
    if pidkazka50:
        print("\t\t\t\t* 50 на 50 *")
    if pidkazkaDzvonok:
        print(f"\t\t\t\t* Дзвінок другу *")
    else:
        print("\t\t\t\tДоступних підказок нема")
    print("\t\t\t\t**********")


def use_podkazki(a, b):
    pods = ""
    global pidkazka50
    global pidkazkaDzvonok
    question = input("Хочете використати підказку?")
    if question == "так" or question == "Так":
        if pidkazka50 == False and pidkazkaDzvonok == False:
            print("Немає доступних підказок")
        elif pidkazka50 == True and pidkazkaDzvonok == True:
            pods = input("50 на 50 чи Дзвінок другу?")
        elif pidkazka50 == True and pidkazkaDzvonok == False:
            pods = input("50 на 50?")
        elif pidkazka50 == False and pidkazkaDzvonok == True:
            pods = input("Дзвінок другу?")
        if pods == "50 на 50":
            print(f"1. {a}, \t2. {b}")
            pidkazka50 = False
        elif pods == "Дзвінок другу":
            print(f"1.{b}")
            pidkazkaDzvonok = False
    elif question == "Ні" or question == "ні":
        print("Окей, не використовуємо підказки")
    else:
        print("Не коректний вибір.")


def question(question_number, question, a1, a2, a3, a4):
    print(f"Питання №{question_number}")
    print(question)
    print(f"1. {a1}\t 2.{a2}")
    print(f"3. {a3}\t 4.{a4}")


def loose(n_summa):
    print("Жаль, але ви проиграли!")
    print(f"Ваш виграш - {n_summa} грн")


player_name = input("Привіт, як тебе звати? ")
pidkazka50 = True
pidkazkaDzvonok = True
n_summa = 0
summa = 0
Continue = True

start(player_name)
player_info(player_name, pidkazka50, pidkazkaDzvonok, n_summa, summa)

question1 = "Який континент являє собою тільки одну країну?"
question(1, question1, "Євразія", "Австралія", "Північна Америка", "Антарктида")
use_podkazki("Євразія", "Австралія")
answer1 = input("Введіть відповідь: ")
if answer1 == "Австралія":
    print("Правильно!")
    summa = 500
else:
    Continue = False

if Continue == False:
    loose(n_summa)
else:
    dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
    question2 = "Де ростуть соняшники?"
    question(2, question2, "На землі", "На дереві", "В небі", "В воді")
    use_podkazki("На дереві", "На землі")
    answer2 = input("Введіть відповідь: ")
    if answer2 == "На землі":
        print("Правильно!")
        summa = 1000
    else:
        Continue = False

    if Continue == False:
        loose(n_summa)
    else:
        dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
        question3 = "Яких валют не існує?"
        question(3, question3, "Гривні", "Долари", "Олег", "Ліри")
        use_podkazki("Ліри", "Олег")
        answer3 = input("Введіть відповідь: ")
        if answer3 == "Олег":
            print("Правильно!")
            summa = 2000
        else:
            Continue = False


if Continue == False:
    loose(n_summa)
else:
    dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
    question4 = "Як називається портрет, намальований з самого себе?"
    question(4, question4, "Самосвал", "Самописка", "Зеркальник", "Автопортрет")
    use_podkazki("Самописка", "Автопортрет")
    answer4 = input("Введіть відповідь: ")
    if answer4 == "Автопортрет":
        print("Правильно!")
        summa = 5000
    else:
        Continue = False

    if Continue == False:
        loose(n_summa)
    else:
        dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
        question5 = "Як називають безпілотний літальний апарат?"
        question(5, question5, "Дрон", "Танк", "Літак", "Аніон")
        use_podkazki("Літак", "Дрон")
        answer5 = input("Введіть відповідь: ")
        if answer5 == "Дрон":
            print("Правильно!")
            summa = 10000
            n_summa = 10000
        else:
            Continue = False

        if Continue == False:
            loose(n_summa)
        else:
            dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
            question6 = "В якій грі не використовують м'яч?"
            question(6, question6, "Баскетбол", "Теніс", "Крікет", "Керлінг")
            use_podkazki("Крікет", "Керлінг")
            answer6 = input("Введіть відповідь: ")
            if answer6 == "Керлінг":
                print("Правильно!")
                summa = 25000
            else:
                Continue = False

            if Continue == False:
                loose(n_summa)
            else:
                dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
                question7 = "Який з цих мостів знаходиться в Києві?"
                question(7, question7, "Кримський", "Дарницький", "Варшавський", "Славутицький")
                use_podkazki("Кримський", "Дарницький")
                answer7 = input("Введіть відповідь: ")
                if answer7 == "Дарницький":
                    print("Правильно!")
                    summa = 100000
                else:
                    Continue = False

                if Continue == False:
                    loose(n_summa)
                else:
                    dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
                    question8 = "Хто з цих людей - письменник?"
                    question(8, question8, "Усейн Болт", "Володимир Зеленський", "Едгар По", "Віталій Кличко")
                    use_podkazki("Володимир Зеленський", "Едгар По")
                    answer8 = input("Введіть відповідь: ")
                    if answer8 == "Едгар По":
                        print("Правильно!")
                        summa = 250000
                    else:
                        Continue = False
                        if Continue == False:
                                loose(n_summa)
                            else:
                                dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
                                question9 = "Хто з цих моряків відкрив Мис Доброї надії?"
                                question(9,question9, "Христофор Колумб", "Бартоломео Діаш", "Джон Брюс", "Васка Дагама")
                                use_podkazki("Христофор Колумб", "Бартоломео Діаш")
                                answer9 = input("Введіть відповідь: ")
                                if answer9 == "Бартоломео Діаш":
                                    print("Правильно!")
                                    summa = 500000
                                else:
                                    Continue = False

                                if Continue == False:
                                    loose(n_summa)
                                else:
                                    dost_podskazki(summa, pidkazka50, pidkazkaDzvonok)
                                    question10 = "В якому році Україна здобула незалежність?"
                                    question(10, question10, "1999", "1995", "2004", "1991")
                                    use_podkazki("1999", "1991")
                                    answer10 = input("Введіть відповідь: ")
                                    if answer10 == "1991":
                                        print("Правильно! Ви виграли!")
                                        n_summa = 1000000
                                        print("Вы виграли супер приз!!!! Вітаємо!!!!")
                                        print("Ваш виграш -", n_summa, "грн")
                                    else:
                                        Continue = False

                                    if Continue == False:
                                        loose(n_summa)