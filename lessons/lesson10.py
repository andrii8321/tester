a = "ім'я:Олександр,вік:16,стать:чоловіча"
b = "ім'я:Владислав,вік:46,стать:чоловіча"

c = {'name':"ОлексAндр",
     "age":16,
     'sx': "Чоловіча"}
c['name'] = "Олексій"
c['age'] = 19
# print("Мене звати", c['name'], ", мені", c['age'],"років")
#
# print(f"Мене звати {c['name']}, мені {c['age']*2} років")

c['country'] = "Ukraine"
c['age'] = None
print(c)
print(c.get('age',"key doesnt exisist"))

