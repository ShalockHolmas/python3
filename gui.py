import tkinter

top = tkinter.Tk()
label = tkinter.Label(top, text="hello world")

label.pack()

qiut = tkinter.Button(top, text='hello world', command=top.quit())
qiut.pack()
tkinter.mainloop()
