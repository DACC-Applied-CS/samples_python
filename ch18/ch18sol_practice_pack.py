from tkinter import *

root = Tk()
root.title("My First GUI")

topFrame = Frame(root)
topFrame.pack()

btn1 = Button(topFrame, text = "Button 1", fg = "red")
btn1.pack(side = LEFT)

btn2 = Button(text = "Button 2", fg = "blue")
btn2.pack()

lbl1 = Label(topFrame, text = "Hello world")
lbl1.pack()




root.mainloop()