from tetrisBoard import TetrisBoard
from tetrisPiece import TetrisPiece
from tkinter import *

WIDTH = 500
HEIGHT = 500
SPEED = 300
SPACE_SIZE = 20
PIECE = "#00FF00"
FALLING = "#FFFFFF"
BACKGROUND = "#000000"

action = None


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2,
                       canvas.winfo_height() / 2,
                       font=('consolas', 70),
                       text="GAME OVER",
                       fill="red", tag="gameover")


def update(board, falling_piece):
    canvas.delete(ALL)
    board = board.get_board()
    x = falling_piece.get_pos_x()
    y = falling_piece.get_pos_y()
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] == 1:
                canvas.create_rectangle(i * SPACE_SIZE,
                                        j * SPACE_SIZE,
                                        i * SPACE_SIZE + SPACE_SIZE,
                                        j * SPACE_SIZE + SPACE_SIZE,
                                        fill=PIECE)
            if x <= i < x + 4 and y <= j < y + 4:
                if falling_piece.get_piece()[j-falling_piece.get_pos_y()][i-falling_piece.get_pos_x()] == 1:
                    canvas.create_rectangle(i * SPACE_SIZE, j * SPACE_SIZE,
                                            i * SPACE_SIZE + SPACE_SIZE, j * SPACE_SIZE + SPACE_SIZE, fill=FALLING)


def turn(board):
    global action
    if action == "left":
        board.move_left()
    elif action == "right":
        board.move_right()
    elif action == "drop":
        board.drop_piece()
    elif action == "rotate":
        board.rotate_piece()
    else:
        board.move_down()

    action = None
    falling_piece = board.get_pieces()[-1]
    update(board, falling_piece)
    window.after(SPEED, turn, board)
    if not board.no_collision():
        game_over()


def set_action(a):
    global action
    action = a


window = Tk()
window.title("Tetris")

canvas = Canvas(window, bg=BACKGROUND,
                height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',
            lambda event: set_action("left"))
window.bind('<Right>',
            lambda event: set_action("right"))
window.bind('<Down>',
            lambda event: set_action("drop"))
window.bind('r',
            lambda event: set_action("rotate"))

init_piece = TetrisPiece(TetrisPiece.generate_piece())
board = TetrisBoard(25, 25, init_piece)
turn(board)

window.mainloop()

