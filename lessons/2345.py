# students = {"Oleksii": 18, "Oksana": 17, "Mykola": 14}
# for key, value in students.items():
#     print(f"Учень {key} має {value} років")
# for name in students:
#     print(f"Учень {name} має {students[name]} років")

# a = (input("put number"))
# b = {"1": "Monday",
#      "2":"Tuesday",
#      "3":"Wednesday",
#      "4":"Thursday",
#      "5":"Friday",
#      "6":"Saturday",
#      "7":"Sunday"}
# if a in b:
#     print(b[a])
# else:
#     print("invalid number")


# a = "alabama"
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(b)


# a = "London is a capital of Great Britain"
# b = {}
# c = ["a","e","y","u","i","o"]
# for i in a.lower() :
#     if i in c :
#         if i in b:
#             b[i] += 1
#         else:
#             b[i] = 1
# print(b)


# a = "London is A capital of Great Britain"
# b = {}
# c = ["a","e","y","u","i","o"]
# for i in a.lower() :
#     if i not in c :
#         b.setdefault(i,0)
#         b[i] += 1
#
# print(b)



def add_or_update_product(key, value):

    products[key] = value
    print(products)
def deleteproduct(key):
    del products[key]
    print(products)

# def updateproduct(key,value):
#
#     products[key] = value
#     print(products)


products = {
    "яблука" : {
        'red':3,
        "green":4
    },
    "груші" : 30,
    "банани" : 20
}
print("Вітаю вас у системі обліку продуктів, оберіть дію")



while True:
    print("1.Додати новий продукт до списку")
    print("2.Оновити кількість продукту")
    print("3.Видалити продукт зі складу")
    print("4.Переглянути наявні продукти")
    print("5.Знайти кількість конкретного  продукту")
    answer = input("6.вийти")
    if answer == "1":
        name = input("введіть назву продукта ")
        amount = input("введіть кількість продукту ")
        add_or_update_product(key = name,value=amount)
        print('ви додали новий продукт')
    elif answer == "2":
        print(products)
        name = input("який продукт ви хочете оновити")
        amount = input("введіть кількість продукту")
        add_or_update_product(key = name,value=amount)
        print("ви оновили кількість")
    elif answer == "3":
        print(products)
        name = input("який продукт ви хочете видалити")
        deleteproduct(name)
    elif answer == "4":

        print(products)
    elif answer == "5":
        name = input('введіть назву продукту ')
        print(products[name])
    else:
        break






































