from tkinter import *
from tkinter.messagebox import showinfo

def test():
    showinfo("Cloudapp","Hello Cloudapp")


root=Tk()
root.title("Cloudapp demo")
root.geometry("250x250")
root.resizable(False,False)

Label(root,text="\n").pack()
Label(root,text="Welcome To CloudAPP Demo").pack()
Label(root,text="\n").pack()
Button(root,text="Click Me",command=test).pack()

root.mainloop()
