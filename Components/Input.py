from tkinter import *


class Input:
    def __init__(self, root, frame, number, callback):
        self.root = root
        self.frame = frame
        self.number = number
        self.callback = callback

        # Configure input frame as a single row with 3 expandable columns
        self.inputFrame = Frame(self.root, self.frame)
        self.inputFrame.grid(column=0, row=0, sticky='WE')
        self.inputFrame.grid_rowconfigure(0, weight=1)
        self.inputFrame.grid_columnconfigure(0, weight=1)
        self.inputFrame.grid_columnconfigure(1, weight=3)
        self.inputFrame.grid_columnconfigure(2, weight=2)
        self.loadInput()

    def loadInput(self):
        # Label to show text
        self.label = Label(self.inputFrame, text="Enter chess side length")
        self.label.grid(column=0, row=0, sticky='NSEW')

        # Entry to input text
        self.input = Entry(self.inputFrame)
        self.input.grid(column=1, row=0, sticky='NSEW')
        self.input.insert(END, self.number)

        # OK button to run the game
        self.submit = Button(
            self.inputFrame,
            text="OK",
            command=lambda: self.callback(self.input.get()),
            background="white"
        )
        self.submit.grid(column=2, row=0, sticky='NSEW')
