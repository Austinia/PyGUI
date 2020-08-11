from tkinter import *

root = Tk()
root.title("GUI TEST")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "please write anything")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Only one line")


def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 첫째줄(1) 0번째 column 부터 가져와라
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
