import customtkinter as cTk
from PIL import Image

# #2FA572 - зеленый
# #1F6AA5 - синий(default)

app = cTk.CTk()
app.iconbitmap(r"C:\Users\Mikhael\PycharmProjects\tic-tac-toe\app\logo.ico")
app.title('Tic-Tac-Toe')
app.resizable(False, False)

players = ["X", "O"]
player = players[0]

cells = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

label = cTk.CTkLabel(master=app, text="Ход " + player, font=("Comic Sans MS", 38), anchor="s")
label.pack(expand=True)

frame = cTk.CTkFrame(master=app)
frame.pack(expand=True, padx=3)


def static_btn():
    for row in range(3):
        for column in range(3):
            cells[row][column].configure(state="")


def next_turn(row, column):
    global player

    if cells[row][column].cget("text") == "" and winner() is False:
        if player == players[0]:
            cells[row][column].configure(text=player)
            if winner() is False:
                player = players[1]
                label.configure(text="Ход " + (players[1]))
            elif winner() is True:
                static_btn()
                label.configure(text=(players[0]) + " выиграли!")

            elif winner() == "Ничья":
                static_btn()
                label.configure(text="Ничья")
        else:
            cells[row][column].configure(text=player)
            if winner() is False:
                label.configure(text="Ход " + (players[0]))
                player = players[0]
            elif winner() is True:
                static_btn()
                label.configure(text=(players[1]) + " выиграли!")
                player = players[0]

            elif winner() == "Ничья":
                static_btn()
                label.configure(text="Ничья")


def winner():
    for row in range(3):
        if cells[row][0].cget("text") == cells[row][1].cget("text") == cells[row][2].cget("text") != "":
            cells[row][0].configure(fg_color="#2FA572")
            cells[row][1].configure(fg_color="#2FA572")
            cells[row][2].configure(fg_color="#2FA572")
            return True
    for column in range(3):
        if cells[0][column].cget("text") == cells[1][column].cget("text") == cells[2][column].cget("text") != "":
            cells[0][column].configure(fg_color="#2FA572")
            cells[1][column].configure(fg_color="#2FA572")
            cells[2][column].configure(fg_color="#2FA572")
            return True
    if cells[0][0].cget("text") == cells[1][1].cget("text") == cells[2][2].cget("text") != "":
        cells[0][0].configure(fg_color="#2FA572")
        cells[1][1].configure(fg_color="#2FA572")
        cells[2][2].configure(fg_color="#2FA572")
        return True
    elif cells[0][2].cget("text") == cells[1][1].cget("text") == cells[2][0].cget("text") != "":
        cells[0][2].configure(fg_color="#2FA572")
        cells[1][1].configure(fg_color="#2FA572")
        cells[2][0].configure(fg_color="#2FA572")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                cells[row][column].configure(fg_color="#2FA572")
        return "Ничья"
    else:

        return False


def new_game():
    global player
    player = players[0]
    label.configure(text="Ход " + player)

    for row in range(3):
        for column in range(3):
            cells[row][column].configure(text="", fg_color="#1F6AA5", state="normal")


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if cells[row][column].cget("text") != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


reset_image = cTk.CTkImage(Image.open(r"ResetBtn.png"), size=(48, 48))
reset_btn = cTk.CTkButton(master=app, text="", image=reset_image, width=64, height=64, command=new_game)
reset_btn.pack(side="top", pady=3)

for row in range(3):
    for column in range(3):
        cells[row][column] = cTk.CTkButton(master=frame, text="", font=("Comic Sans MS", 50), width=96,
                                           height=96,
                                           command=lambda row=row, column=column: next_turn(row, column))
        cells[row][column].grid(row=row + 1, column=column, pady=3, padx=3)

app.mainloop()
