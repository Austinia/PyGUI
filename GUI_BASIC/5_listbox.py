from tkinter import *

root = Tk()
root.title("GUI TEST")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "Apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()


def btncmd():
    # listbox.delete(0) 삭제

    print("There are/is", listbox.size(), "on the list") # 갯수 확인

    print("first to third are", listbox.get(0, 2)) # 항목 확인 (시작 idx, 끝 idx)

    print("you selected", listbox.curselection()) # 선택된 항목 확인 (위치로 반환 ex= (0, 4))




btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
