from tkinter import *
import random
root = Tk()
root.geometry("600x600")
root.title("Random Coolors")
root.config(background = "#87BFFF")
colors = {
    "Yellow Orange":"#FF9505",
    "Pink":"#F07167",
    "Green":"#A7C957",
    "Purple":"#A390E4",
    "Red":"#9A031E"
}
rnd_list = ["Yellow Orange", "Pink", "Green", "Purple", "Red"]
def magic():
    random_number = random.randint(0, 4)
    print(random_number)
    random_color = rnd_list[random_number]
    print(random_color)
    hex_code = colors[random_color]
    print(hex_code)
    root.config(background = hex_code)
btn = Button(text="Change Background Color", command=magic)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
root.mainloop()