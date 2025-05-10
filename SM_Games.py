from tkinter import *

root = Tk()
root.configure(bg="white")
root.title("무인도 살인사건 추리게임")
root.geometry("1700x900")

canvas = Canvas(root, width=700, height=700)
canvas.pack()

text = Text(root, width=15, height=12)
scrollbar = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)

text.pack(sid="left")
scrollbar.pack(side="right", fill="y")

root.mainloop()