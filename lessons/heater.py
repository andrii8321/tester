import random
class Heater:
    def __init__(self,name,volume,status='off',mode='normal',number=None):
        self.name = name
        self.volume = volume
        self.status = status
        if number:
            self.number=number
        else:
            self.number = self.serial_number()
        self.mode = mode

    def serial_number(self):
        number = random.randint(1,256)
        letter_list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f']
        letter = random.choice(letter_list)
        serial_number = f'{number}{letter}{number}{letter}'
        return serial_number

    def on(self):
        if self.status.upper() == "ON":
            print("heater is already on")
        self.status = "ON"
    def set_mode(self):
        if self.mode == "normal":
            print("mode: normal")
        self.mode = "normal"


    def off(self):
        if self.status.upper() == "OFF":
            print("heater is alredy off")
        self.status = "OFF"
    def info(self):
        print(f'model:{self.name}\n'
              f'volume is {self.volume}\n'
              f'heater is {self.status}\n'
              f'serial number: {self.number}')
    def __repr__(self):
        return f'It`s {self.name}'