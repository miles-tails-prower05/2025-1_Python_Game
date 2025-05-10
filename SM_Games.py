from tkinter import *

root = Tk()
root.configure(bg="white")
root.title("무인도 살인사건 추리게임")
root.geometry("1090x1080")

canvas = Canvas(root, width=700, height=700)
canvas.pack()

scrollbar=Tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

root.mainloop()