from tkinter import *

from Components.Input import *
from Components.Board import *

import os

os.system("cls")


class Chess:
    def __init__(self):
        self.root = Tk()
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)
        self.n = IntVar()

        self.root.title("N Chess Queens Puzzle")
        self.root.iconbitmap("Components/images/queen_crown.ico")

        # Set window width and height
        self.w, self.h = 800, 800
        self.root.geometry("%dx%d" % (self.w, self.h))

        # Set full screen mode on F11 with exit on Escape key
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)

        # Set grid in one column and two rows for Input and Board
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=20)

        # Load input and board with nxn side length
        self.loadChess(self.n.get())

        self.root.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)

    # Load chess class
    def loadChess(self, number):
        # Frame for input on top
        self.inputFrame = Frame(self.root, background="blue")
        self.inputFrame.grid(sticky=NSEW, column=0, row=0)

        # Set the nxn board side length and load Input and the board
        self.n.set(number)
        if number == 0:
            self.input = Input(
                self.root,
                self.inputFrame,
                "",
                self.loadChess
            )
        else:
            self.input = Input(
                self.root,
                self.inputFrame,
                self.n.get(),
                self.loadChess
            )

        # Frame for board below input
        self.boardFrame = Frame(self.root, background="red")
        self.boardFrame.grid(sticky=NSEW, column=0, row=1)

        self.board = Board(self.root, self.boardFrame, self.n.get())
