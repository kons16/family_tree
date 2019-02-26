import tkinter as tk
from tkinter import *


# 名前追加ボタンを押されたときの処理
def addNameValue(event):
    global label_name, setx, sety, name_list
    newName = nameBox.get()
    label_name = tk.Label(canvas, text=newName)
    label_name.bind("<Button-1>", showMenu)

    # addXX関数でセットされた位置に名前を配置
    label_name.place(x=setx, y=sety)

    # 名前入力欄をクリアする
    nameBox.delete(0, tk.END)


def showMenu(event):
    global label_name, setx, sety, label_width
    # set座標にクリックしたイベントの位置を代入
    setx = event.widget.winfo_rootx() - 5
    sety = event.widget.winfo_rooty() - 50
    label_width = event.widget.winfo_width()
    menu.post(event.x_root, event.y_root)


def addFather():
    global setx, sety, label_width
    # 家系図への線を描く
    canvas.create_line(setx+label_width/2, sety,
                       setx+label_width/2, sety-40,
                       setx+label_width/2-40, sety-40)
    # addFatherを押したラベルの座標からfatherをセットする位置を決める
    setx = setx - 45 - label_width/2
    sety = sety - 50


def addMother():
    global setx, sety, label_width

    canvas.create_line(setx+label_width/2, sety,
                       setx+label_width/2, sety-40,
                       setx+label_width/2+40, sety-40)

    setx = setx + 30 + label_width/2
    sety = sety - 50


def addBig():
    global setx, sety, label_width

    canvas.create_line(setx+label_width/2, sety,
                       setx+label_width/2, sety-20,
                       setx+label_width/2-60, sety-20,
                       setx+label_width/2-60, sety)

    setx = setx - 80 + label_width/2
    sety = sety


def addLittle():
    global setx, sety, label_width

    canvas.create_line(setx+label_width/2, sety,
                       setx+label_width/2, sety-20,
                       setx+label_width/2+60, sety-20,
                       setx+label_width/2+60, sety)

    setx = setx + 45 + label_width/2
    sety = sety


root = tk.Tk()
root.iconbitmap('test.ico')
root.title("Family Tree")
root.geometry("500x500")

# 初期値
mode = 'me'
setx = 250
sety = 250
label_width = 0

menu = Menu(root, tearoff=False)
menu.add_command(label="父親を追加", command=addFather)
menu.add_command(label="母親を追加", command=addMother)
menu.add_command(label="兄姉を追加", command=addBig)
menu.add_command(label="弟妹を追加", command=addLittle)

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
