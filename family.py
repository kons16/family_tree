import sys
import tkinter as tk
from tkinter import *


# 名前追加ボタンを押されたときの処理
def addNameValue(event):
    global nameLbl
    newName = nameBox.get()
    nameLbl = tk.Label(canvas, text=newName)
    nameLbl.bind("<Button-2>", showMenu)
    nameLbl.place(x=250, y=250)


def showMenu(event):
    menu.post(event.x_root, event.y_root)


def addFather(event):



def deleteName():
    nameLbl.destory()


root = tk.Tk()
root.iconbitmap('test.ico')
root.title("家系図シュミレーター")
root.geometry("500x500")

menu = Menu(root, tearoff=False)
menu.add_command(label="削除", command=deleteName)
menu.add_command(label="父親を追加", command=addFather)

# キャンバス
canvas = tk.Canvas(root, width=500, height=500)
canvas.place(x=0, y=0)

# 名前
nameBox = tk.Entry(width=20)
nameBox.insert(tk.END, "")
nameBox.pack(anchor="se", side="left")

# 名前追加ボタン
addBtn = tk.Button(text="追加", width=8)
# <Button-1>は左クリック
addBtn.bind("<Button-1>", addNameValue)
addBtn.pack(anchor="se", side="left")

root.mainloop()
