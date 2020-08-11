from tkinter import *

root = Tk()
root.title("GUI TEST")
root.geometry("640x480")

label1= Label(root, text="Hello World")
label1.pack()

photo = PhotoImage(file="check_icon.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="See Ya")

    global photo2  # 메모리 청소 당하지 않게 전역 변수로
    photo2 = PhotoImage(file="incorrect_icon.png")
    label2.config(image=photo2)


btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()
