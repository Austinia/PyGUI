from tkinter import *

root = Tk()
root.title("GUI TEST")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # 여백 개념, 크기 유동적
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")  # 크기고정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="check_icon.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭 됨")


btn7 = Button(root, text="동작버튼", command=btncmd)
btn7.pack()

root.mainloop()