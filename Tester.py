from tkinter import *

tk = Tk()
tk.title("Simple Test")

button = Button(tk, text="Test", state=DISABLED)
button.pack()

tk.mainloop()
