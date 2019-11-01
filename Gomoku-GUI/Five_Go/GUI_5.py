from tkinter import *
from PIL import ImageTk, Image
import os



def createboard():
    boardrow=[]
    board=[]
    for x in range(15):
        for y in range(15):
            boardrow.append("O")
        board.append(boardrow)
        boardrow=[]
    return board


board=createboard()
friend_win = None
button = None
listButtons = []

times = 0
win=""

# imgblack = ImageTk.PhotoImage(Image.open("Octocorn_Black.png"))
# img_white = ImageTk.PhotoImage(Image.open("Octocorn_White.png"))
# img_black_win = ImageTk.PhotoImage(Image.open("Octocorn_Black_Win.png"))
# img_white_win = ImageTk.PhotoImage(Image.open("Octocorn_White_Win.png"))






def friendGUI():
    global friend_win
    global button
    global listButtons
    global x
    global y
    global button_new
    global button_undo
    global l_turn
    global l_pic
    global times



    friend_win = Tk()
    friend_win.title("Super Gokuma")

    f1 = Frame(friend_win, padx=10, pady=10)
    f1.grid(row=1,column=1)

    listButtons = []
    listrow = []

    for x in range(15):
        for y in range(15):

            button = Button(f1,text="",width=2,height=1,command=lambda x=x, y=y: click_button(x,y))
            button.grid(row=x, column=y)
            listrow.append(button)

        listButtons.append(listrow)
        listrow = []

    f2 = Frame(friend_win,padx=10, pady=10)
    f2.grid(row=1,column=2)

    img = ImageTk.PhotoImage(Image.open("Octocorn_Black.png"))
    l_pic = Label(f2, image=img)
    l_pic.grid(row=1, column=1)

    l_turn = Label(f2,text="Black, your turn!",width=20)
    l_turn.grid(row=2, column=1,pady=10)


    button_undo = Button(f2,text="Undo",width=4,command=button_undo)
    button_undo.grid(row=3, column=1,pady=10)



    button_new = Button(f2,text="New",width=4,command=button_new)
    button_new.grid(row=4, column=1,pady=10)


    friend_win.mainloop()




def check_win(aboard):
    global win
    global board
    global button_signal
    global l_turn
    global l_pic
    global f2


    for row in range(15):
        for col in range(11):
            if board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]==board[row][col+4]=="B":
                win="black"
                print("Black Wins")
                l_turn["text"] = "And the winner is ... BLACK!"

            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == board[row][col + 4] == "W":
                win="white"
                print("White Wins")
                l_turn["text"] = "And the winner is ... WHITE!"

    for row in range(11):
        for col in range(15):
            if board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]==board[row+4][col]=="B":
                win="black"
                print("Black Wins")
                l_turn["text"]="And the winner is ... BLACK!"
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == board[row+4][col] == "W":
                win="white"
                print("White Wins")
                l_turn["text"]="And the winner is ... WHITE!"

    for row in range(11):
        for col in range(11):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4] == "B":
                win = "black"
                print("Black Wins")
                l_turn["text"] = "And the winner is ... BLACK!"
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4] == "W":
                win = "white"
                print("White Wins")
                l_turn["text"] = "And the winner is ... WHITE!"

    for row in range(4,15):
        for col in range(11):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == board[row-4][col+4] == "B":
                win = "black"
                print("Black Wins")
                l_turn["text"] = "And the winner is ... BLACK!"
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == board[row-4][col+4] == "W":
                win = "white"
                print("White Wins")
                l_turn["text"] = "And the winner is ... WHITE!"



def click_button(x,y):
    global listButtons
    global times
    global board
    global row
    global col
    global l_pic
    global f2
    global img
    global win
    global button_undo

    row = x
    col = y

    if listButtons[x][y]["text"]=="" and win == "":

        if times%2 == 0:
            listButtons[x][y]["text"]="1"
            board[x][y] = "B"
            l_turn["text"]="White, your turn!"
            img2 = ImageTk.PhotoImage(Image.open("Octocorn_White.png"))
            l_pic.configure(image=img2)
            l_pic.image = img2


            # l_pic["image"]= ImageTk.PhotoImage(Image.open("Octocorn_Black.png"))

        if times%2 == 1:
            listButtons[x][y]["text"]="2"
            board[x][y] = "W"
            l_turn["text"]="Black, your turn!"
            img1 = ImageTk.PhotoImage(Image.open("Octocorn_Black.png"))
            l_pic.configure(image=img1)
            l_pic.image = img1

            # l_pic["image"]=ImageTk.PhotoImage(Image.open("Octocorn_White.png"))

        times += 1

    check_win(board)

    if win=="black":
        img3 = ImageTk.PhotoImage(Image.open("Octocron_Black_Win.png"))
        l_pic.configure(image=img3)
        l_pic.image = img3
        button_undo["fg"]="grey"
    if win=="white":
        img4 = ImageTk.PhotoImage(Image.open("Octocorn_White_Win.png"))
        l_pic.configure(image=img4)
        l_pic.image = img4
        button_undo["fg"] = "grey"



    # print(x,y)
    # print(times)
    # print(win)


def button_undo():
    global times
    global listButtons
    global board
    global row
    global col
    global l_pic
    global l_turn
    global button_undo


    if listButtons[row][col]["text"]!="" and win=="":
        listButtons[row][col]["text"]=""
        board[row][col]="O"
        times-=1

        if times%2==1:
            l_turn["text"]="White, Your turn!"
            img2 = ImageTk.PhotoImage(Image.open("Octocorn_White.png"))
            l_pic.configure(image=img2)
            l_pic.image = img2
        if times%2==0:
            l_turn["text"]="Black, Your turn!"
            img1 = ImageTk.PhotoImage(Image.open("Octocorn_Black.png"))
            l_pic.configure(image=img1)
            l_pic.image = img1



def button_new():
    global times
    global listButtons
    global board
    global l_turn
    global l_pic
    global win
    global button_undo

    win = ""
    times=0
    l_turn["text"]="Black, your turn!"

    for x in range(15):
        for y in range(15):
            board[x][y]="O"

    for x in listButtons:
        for y in x:
            y["text"] = ""

    l_turn["text"] = "Black, Your turn!"
    img1 = ImageTk.PhotoImage(Image.open("Octocorn_Black.png"))
    l_pic.configure(image=img1)
    l_pic.image = img1

    button_undo["fg"] = "black"


    print(win)
    print(board)
    print(times)


friendGUI()

