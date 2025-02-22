import random
gallows = [
"",
"""
|
|
|
|
|
|
---
""",
"""
------
|  |
|
|
|
|
|
---
""",
"""
------
|  |
|  O
|
|
|
|
---
""",
"""
------
|  |
|  O
| /|\
|
|
|
---
""",

"""
------
|  |
|  O
| /|\
| / \
|
|
---
"""]
words = ["мопед", "аймал", "ферма", "молоко", "фіалка", "вантуз", "абрикос", "табурет"]
word = random.choice(words)
string = "_" * len(word)
wrong = 0
used = []
print(word)
print(string)

while wrong < 5 and string != word:
    print("Ви використали літери:", used)
    print("Слово виглядає так:", string)
    let = input("Введіть літеру: ")
    while let in used:
        print("Ви вже вводили літеру", let)
        let = input("Введіть літеру: ")
    used.append(let)
    if let in word:
        new_string = ""
        for i in range(len(word)):
            if let == word[i]:
                new_string += let
            else:
                new_string += string[i]
        string = new_string
    else:
        print("Літери", let, "немає у слові")
        wrong += 1
        print(gallows[wrong])
    if wrong == 5:
        print("Ви програли, Вас повісили")
    else:
        print("Ви перемогли")
print("Загадане слово було:", word)

print("hello git")
print('h')









