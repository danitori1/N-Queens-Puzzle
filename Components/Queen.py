from tkinter import *
from PIL import ImageTk, Image


class Queen:
    def __init__(self, root, frame, column, row):
        self.root = root
        self.frame = frame
        self.column = column
        self.row = row

        self.queenFrame = Frame(self.frame)
        self.queenFrame.grid(column=self.column, row=self.row, sticky="NSWE")

        # Get the chess_queen_logo.png image and resize it
        self.queenFrame.update()
        img = ImageTk.PhotoImage(
            Image.open("Components/images/chess_queen_logo.png").resize(
                (int(round(self.queenFrame.winfo_height()/4)),
                 int(round(self.queenFrame.winfo_width())/4)),
                Image.ANTIALIAS
            )
        )

        # Put the image on the Label
        self.queen = Label(self.queenFrame, image=img)
        self.queen.image = img
        self.queen.pack(fill=BOTH, expand=True)
