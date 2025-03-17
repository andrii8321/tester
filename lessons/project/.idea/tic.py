import tkinter as tk
from PIL import Image, ImageTk
def change_bg():
    global photo
    image = Image.open("cross.png")
    image = image.resize((button.winfo_width(), button.winfo_height()))
    photo = ImageTk.PhotoImage(image)
    button.config(image=photo, text="", compound="center")


root = tk.Tk()
root.title("Смена фона кнопки")

button = tk.Button(root, text="Нажми меня", command=change_bg)
button.pack(pady=20, padx=20)

root.mainloop()