import tkinter as tk
from tkinter import *


# 名前追加ボタンを押されたときの処理
def addNameValue(event):
    global label_name, setx, sety
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
    setx = label_name.winfo_rootx() - 5
    sety = label_name.winfo_rooty() - 50
    label_width = label_name.winfo_width()
    menu.post(event.x_root, event.y_root)


def addFather():
    global setx, sety, label_width
    # 家系図への線を描く
    canvas.create_line(setx+label_width/2, sety, setx+label_width/2,
                       sety-40, setx+label_width/2-40, sety-40)
    # addFatherを押したラベルの座標からfatherをセットする位置を決める
    setx = setx - 45 - label_width/2
    sety = sety - 50


def addMother():
    global setx, sety, label_width
    # 家系図への線を描く
    canvas.create_line(setx+label_width/2, sety, setx+label_width/2,
                       sety-40, setx+label_width/2+40, sety-40)
    # addFatherを押したラベルの座標からfatherをセットする位置を決める
    setx = setx + 45 + label_width/2
    sety = sety - 50


def deleteName():
    label_name.destory()


root = tk.Tk()
root.iconbitmap('test.ico')
root.title("家系図シュミレーター")
root.geometry("500x500")

# 初期変数
mode = 'me'
setx = 250
sety = 250
label_width = 0

menu = Menu(root, tearoff=False)
menu.add_command(label="父親を追加", command=addFather)
menu.add_command(label="母親を追加", command=addMother)

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
