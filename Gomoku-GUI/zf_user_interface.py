from tkinter import *


def create_board():
    row = []
    col = []
    for x in range(15):
        for y in range(15):
            row.append("0")
        col.append(row)
    return col


def user_interface():
    global win
    global button
    global mine_counts
    global face
    global time_counts

    win = Tk()
    win.title("Frog Wrapper")

    """
    Top frame
    """
    f0 = Frame(win, padx=18, pady=4)
    f0.grid(row=1, column=1)

    mine_counts = Button(f0, text="000", width=4, height=2)
    mine_counts.grid(row=1, column=0)

    face = Button(f0, text="(#_#)", width=4, height=2)
    face.grid(row=1, column=1)

    time_counts = Button(f0, text="000", width=4, height=2)
    time_counts.grid(row=1, column=2)

    """
    Bottom frame
    """
    f1 = Frame(win, padx=20, pady=20)
    f1.grid(row=2, column=1)

    for x in range(9):
        for y in range(9):
            button = Button(f1, text="", width=2, height=1)
            button.grid(row=x, column=y)

    win.mainloop()


user_interface()