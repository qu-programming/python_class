# coding: utf-8
# import sys
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("janken")
root.geometry("700x500")

# button processing


def rock(event):
    global honda, label
    honda.set("パー\n俺の勝ち。なんで負けたか明日まで考えといてくださいw")
    label.pack()


def scissors(event):
    global honda, label
    honda.set("グー\n俺の勝ち。負けは次に繋がるチャンスですw")
    label.pack()


def paper(event):
    global honda, label
    honda.set("チョキ\n俺の勝ち。たかがじゃんけん、そう思ってないですか?w")
    label.pack()


# label
honda = tkinter.StringVar()
honda.set("じゃーんけーん")
static1 = tkinter.Label(root, textvariable=honda, font=("", 20))
static1.pack()

# photo
img = Image.open("h.png")
tkimg = ImageTk.PhotoImage(img)
label = tkinter.Label(root, image=tkimg, bg="black")

# button
b1 = tkinter.Button(text="グー", font=("", 16), width=20)
b1.bind("<Button-1>", rock)

b2 = tkinter.Button(text="チョキ", font=("", 16), width=20)
b2.bind("<Button-1>", scissors)

b3 = tkinter.Button(text="パー", font=("", 16), width=20)
b3.bind("<Button-1>", paper)

b3.pack(anchor="s", side="bottom")
b2.pack(anchor="s", side="bottom")
b1.pack(anchor="s", side="bottom")

# mainloop
root.mainloop()
