from tkinter import *


class Square:
    def __init__(self, root, frame, column, row, color, disabled, callback):
        self.root = root
        self.frame = frame
        self.column = column
        self.row = row
        self.color = color
        self.disabled = disabled
        self.callback = callback

        # If the square is disabled show the red square, if not, show a button that when it's clicked, it creates a queen on it
        if self.disabled:
            self.square = Label(
                self.frame,
                background=self.color,
                borderwidth=2,
                relief="groove"
            )
        else:
            self.square = Button(
                self.frame,
                background=self.color,
                command=lambda: self.callback(
                    row=self.row,
                    column=self.column
                )
            )

        self.square.grid(column=self.column, row=self.row, sticky="NSWE")
