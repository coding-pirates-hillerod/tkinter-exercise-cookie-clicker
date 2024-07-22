from tkinter import Tk, PhotoImage, Button, Label

counter = 0


def btn_click():
    global counter
    counter += 1
    counter_label.config(text=counter)


root = Tk()
root.title("My Awesome 'Cookie Clicker'")

image = PhotoImage(file="./cookie.gif")

btn = Button(root, image=image, command=btn_click)
btn.pack()

counter_label = Label(root, text=counter)
counter_label.pack()


root.mainloop()
