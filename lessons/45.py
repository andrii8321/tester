import random

from heater import Heater

first = Heater(name="siemense",volume='2 liter',status='off',mode='rocket6',number="jvn4iwutb3gybvwuqb3")
second = Heater(name="philips",volume="3 LITER",)
third = Heater(name="samsung",volume="5 liter" ,)


heaters = [first,second,third]

choice_heater = 1

heaters[choice_heater].info()

while True:

    print('1)створити чайник')
    print('2)переглянути інформацію про поточний чайник')
    print('3)обрати чайник зі списку')
    print('4)включити чайник')
    print('5)вимкнути чайник')
    print('6)режим роботи')
    print('7)інформація про всі чайники')
    print('8)вихід з гри')
    choice = input("Оберіть дію")
    if choice == "4":
        heaters[choice_heater].on()
        print(f'heater {heaters[choice_heater].name} is on ')

    elif choice == "5":
        heaters[choice_heater].off()
        print(f'heater {heaters[choice_heater].name} is off ')
    elif choice == "6":
        print(first.mode)

    elif choice == "7":
        for heater in heaters:
            heaters[choice_heater].info()
            print('      ')

    elif choice == "1":
        model = input("put a model")
        volume = input("create volume")
        second = Heater(name=model,volume=volume,)
        heaters.append(second)
        print(heaters)
    elif choice == "3":
        for i in heaters:
            number = heaters.index(i)
            print(f'{number+1}.{i.name}')
        choice_heater = int(input("which one do you prefer?"))-1

    elif choice == "2":
        choose = int(input("which heater do you want to get?"))
        if choose >= 1 and choose <= len(heaters):
            print(heaters[choose-1])
        else:
            print("wrong number")
    elif choice == "8":
        break
    else:
        print("wrong number")



















