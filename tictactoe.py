from tkinter import *
import tkinter.messagebox

# Initialize the main window
tk = Tk()
tk.title("Tic Tac Toe Multiplayer")

# Initialize variables for player names and turn tracking
playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()

# Create entry fields for player names
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

# Track the state of the game
bclick = True
flag = 0

# Function to disable all buttons after a win or tie
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

# Function to handle button clicks and game logic
def btnClick(buttons):
    global bclick, flag, playerB, playerA
    if buttons["text"] == " " and bclick:
        buttons["text"] = "X"
        buttons["bg"] = "#FF6666"
        bclick = False
        playerA = p1.get() + " Wins!"
        playerB = p2.get() + " Wins!"
        checkforwin()
        flag += 1
    elif buttons["text"] == " " and not bclick:
        buttons["text"] = "O"
        buttons["bg"] = "white"
        bclick = True
        checkforwin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Button already clicked")
        buttons["bg"] = "white"

# Function to check for a win or tie
def checkforwin():
    global flag
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        disableButton()
        tkinter.messagebox.showinfo("Tic Tac Toe", playerA)
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        disableButton()
        tkinter.messagebox.showinfo("Tic Tac Toe", playerB)
    elif flag == 8:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie!")

# Create buttons for the Tic Tac Toe grid
button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

# Run the main loop to start the game
tk.mainloop()
