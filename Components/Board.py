from tkinter import *
from Components.Square import *
from Components.Queen import *
from random import randrange


class Board:
    def __init__(self, root, frame, number):
        self.root = root
        self.frame = frame
        self.number = number
        self.disabled = {
            "rows": [],
            "columns": [],
            "up_diagonals": [],
            "down_diagonals": []
        }

        # Divide main frame in two rows for score and board
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=10)

        # Score Frame
        self.scoreFrame = Frame(self.frame)
        self.scoreFrame.grid(sticky=NSEW, column=0, row=0)
        self.scoreFrame.grid_rowconfigure(0, weight=1)
        self.scoreFrame.grid_rowconfigure(1, weight=1)
        self.scoreFrame.grid_columnconfigure(0, weight=1)
        self.scoreFrame.grid_columnconfigure(1, weight=1)

        # Board Frame
        self.boardFrame = Frame(self.frame)
        self.boardFrame.grid(sticky=NSEW, column=0, row=1)

        self.loadBoard()

    def loadBoard(self):

        for child in self.boardFrame.winfo_children():
            child.destroy()

        self.queensCount = 0
        self.freeSquares = []

        # Divide the grid in nxn squares
        for x in range(self.number):
            for y in range(self.number):
                self.boardFrame.grid_rowconfigure(y, weight=1)
                self.boardFrame.grid_columnconfigure(x, weight=1)

                # When a new queen is created, the row(y), column(x), sum of row and column, and difference between row and column are stored in arrays in self.disabled dict
                # To check if the square is disabled:
                # - The square has to be in the same row and column as the queen.
                # - The sum(x+y) has to be the same for the up-right(/) direction diagonal.
                # - The diffenrence(x-y) has to be the same for the down-right(\) direction diagonal.

                # If the square is a queen, it has to meet all the requirements, and all the indexes in the different arrays has to be the same
                if (
                    x in self.disabled["columns"] and
                    y in self.disabled["rows"] and
                    x+y in self.disabled["up_diagonals"] and
                    x-y in self.disabled["down_diagonals"] and
                    self.disabled["columns"].index(x) ==
                    self.disabled["rows"].index(y) ==
                    self.disabled["up_diagonals"].index(x+y) ==
                    self.disabled["down_diagonals"].index(x-y)
                ):
                    self.queensCount += 1
                    Queen(
                        self.root,
                        self.boardFrame,
                        column=x,
                        row=y
                    )

                # If the square is not a queen but meet any other requirement then is a square where it has the possibility to be killed by other queen
                elif (
                    x in self.disabled["columns"] or
                    y in self.disabled["rows"] or
                    x+y in self.disabled["up_diagonals"] or
                    x-y in self.disabled["down_diagonals"]
                ):
                    Square(
                        self.root,
                        self.boardFrame,
                        column=x,
                        row=y,
                        color="red",
                        disabled=True,
                        callback=self.handleClick
                    )

                # If no requirement is acomplished, then the queen in this square is out of danger of being killed
                else:
                    # Save square in freeSquares list
                    self.freeSquares.append({
                        "row": y,
                        "column": x
                    })

                    # Color the square depending if the sum number is even or add
                    if (x+y) % 2 == 0:
                        color = "yellow"
                    else:
                        color = "black"
                    Square(
                        self.root,
                        self.boardFrame,
                        column=x,
                        row=y,
                        color=color,
                        disabled=False,
                        callback=self.handleClick
                    )

        # Text to show number of queens
        self.queensInfo = Label(
            self.scoreFrame,
            text="Queens: " + str(self.queensCount)
        )
        self.queensInfo.grid(sticky=NSEW, column=0, row=0)

        # Text to show number of free squares available
        self.squaresInfo = Label(
            self.scoreFrame,
            text="Free squares: " + str(len(self.freeSquares))
        )
        self.squaresInfo.grid(sticky=NSEW, column=0, row=1)

        # Button to load the previous state
        self.undoButton = Button(
            self.scoreFrame,
            text="Undo",
            command=lambda: self.handleBack()
        )
        self.undoButton.grid(sticky=NSEW, column=1, row=0)

        # Button to load a solution automatically for the board
        self.solutionButton = Button(
            self.scoreFrame,
            text="Solution",
            command=lambda: self.handleSolution()
        )
        self.solutionButton.grid(sticky=NSEW, column=1, row=1)

        if self.number > 0 and self.queensCount == self.number:
            # Win text to show when there's N queens
            self.squaresInfo = Label(
                self.scoreFrame,
                text="YOU WIN!",
                background="green"
            )
        elif self.number > 0 and len(self.freeSquares) == 0:
            # Lose text to show when there's no freeSquares
            self.squaresInfo = Label(
                self.scoreFrame,
                text="YOU LOSE!",
                background="red"
            )

        self.squaresInfo.grid(sticky=NSEW, column=0, row=1)

    # Function to add a new queen

    def addQueen(self, row, column):
        # Add at the begining of the array the queen's values
        self.disabled["rows"].insert(0, row)
        self.disabled["columns"].insert(0, column)
        self.disabled["up_diagonals"].insert(0, column + row)
        self.disabled["down_diagonals"].insert(0, column - row)

    # Function to do when click and reload board

    def handleClick(self, row, column):
        self.addQueen(row, column)
        self.loadBoard()

    # Function to undo changes

    def handleBack(self):
        # Delete the latest queen values
        if len(self.disabled["rows"]) > 0:
            del self.disabled["rows"][0]
            del self.disabled["columns"][0]
            del self.disabled["up_diagonals"][0]
            del self.disabled["down_diagonals"][0]
            self.loadBoard()

    # Function to create a solution automatically

    def handleSolution(self):

        # Delete previous queens
        self.disabled["rows"] = []
        self.disabled["columns"] = []
        self.disabled["up_diagonals"] = []
        self.disabled["down_diagonals"] = []

        # Follow different rules depending on the n number
        if self.number == 8:
            # Special case 9 that doesn't follow any rule
            eight_queens = [[0, 0], [1, 6], [2, 4], [3, 7],
                            [4, 1], [5, 3], [6, 5], [7, 2]]
            for queen in eight_queens:
                self.addQueen(row=queen[0], column=queen[1])

        elif self.number == 9:
            # Special case 9 that doesn't follow any rule
            eight_queens = [[0, 4], [1, 6], [2, 8], [3, 3],
                            [4, 1], [5, 7], [6, 5], [7, 2], [8, 0]]
            for queen in eight_queens:
                self.addQueen(row=queen[0], column=queen[1])

        elif self.number % 2 == 0:
            # Odd numbers follow a double diagonal starting on the (0,1) square
            row = 0
            column = 1
            diagonal = 1
            while diagonal <= 2:
                while column <= (self.number-1):
                    self.addQueen(row=row, column=column)
                    row += 1
                    column += 2

                diagonal += 1
                column = 0

        else:
            # Even numbers follow a double diagonal starting on the (0,0) square
            row = 0
            column = 0
            diagonal = 1
            while diagonal <= 2:
                while column <= (self.number-1):
                    print(row, column)
                    self.addQueen(row=row, column=column)
                    row += 1
                    column += 2

                diagonal += 1
                column = 1

        self.loadBoard()
