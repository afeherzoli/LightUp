from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, Font, nametofont
from game import Game
from square import Square as Sqr

SIZE = 7

class Gui():

    def __init__(self) -> None:
        self.game = Game()
        self.root = Tk()
        self.root.title("Light Up")
        self.root.configure(background="black")
        self.root.geometry("364x392")
        self.root.minsize(350, 370)
        self.root.maxsize(350, 370)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        myFont = nametofont("TkDefaultFont")
        myFont.configure(weight='bold')
        self.root.option_add("*Font", myFont)
        self.initialzieBoard()


    def mainloop(self):
        self.root.mainloop()


    def initialzieBoard(self):
        for rows in range(SIZE):
            for columns in range(SIZE):
                lbl = Label(self.root, height=3, width=6, fg="black", bg="gray")
                lbl.grid(row=rows, column=columns, padx=(1, 1), pady=(1,1))
                lbl['text'] = self.__symbolAt(rows, columns)
                lbl['bg'] = self.__bgAt(rows, columns)
                if self.__symbolAt(rows, columns) == "":
                    lbl.bind("<Button-1>", lambda e, a=rows, b=columns: self.button_click(1, a, b))
                    lbl.bind("<Button-3>", lambda e, a=rows, b=columns: self.button_click(3, a, b))
                
    
    def refreshBoard(self):
        for rows in range(SIZE):
            for columns in range(SIZE):
                widget = self.root.grid_slaves(row=rows, column=columns)[0]
                widget['text'] = self.__symbolAt(rows, columns)
                widget['bg'] = self.__bgAt(rows, columns)


    def __symbolAt(self, rows, columns):
        if self.game.grid[rows][columns] == Sqr.EMPTY:
            return ''
        elif self.game.grid[rows][columns] == Sqr.BLOCK:
            return ' '
        elif self.game.grid[rows][columns] == Sqr.FOUR:
            return '4'
        elif self.game.grid[rows][columns] == Sqr.THREE:
            return '3'
        elif self.game.grid[rows][columns] == Sqr.TWO:
            return '2'
        elif self.game.grid[rows][columns] == Sqr.ONE:
            return '1'
        elif self.game.grid[rows][columns] == Sqr.ZERO:
            return '0'
        elif self.game.grid[rows][columns] == Sqr.LIGHT:
            return 'O'
        elif self.game.grid[rows][columns] == Sqr.LIT:
            return ' '
        elif self.game.grid[rows][columns] == Sqr.NOLIGHT:
            return 'x'
        elif self.game.grid[rows][columns] == Sqr.LITNOLIGHT:
            return 'x'


    def __bgAt(self, rows, columns):
        if self.game.grid[rows][columns] == Sqr.EMPTY:
            return 'white'
        elif self.game.grid[rows][columns] == Sqr.BLOCK:
            return 'gray'
        elif self.game.grid[rows][columns] == Sqr.FOUR:
            return 'gray'
        elif self.game.grid[rows][columns] == Sqr.THREE:
            return 'gray'
        elif self.game.grid[rows][columns] == Sqr.TWO:
            return 'gray'
        elif self.game.grid[rows][columns] == Sqr.ONE:
            return 'gray'
        elif self.game.grid[rows][columns] == Sqr.ZERO:
            return 'gray'
        elif self.game.grid[rows][columns] == Sqr.LIGHT:
            return 'yellow'
        elif self.game.grid[rows][columns] == Sqr.LIT:
            return 'yellow'
        elif self.game.grid[rows][columns] == Sqr.NOLIGHT:
            return 'white'
        elif self.game.grid[rows][columns] == Sqr.LITNOLIGHT:
            return 'yellow'


    def button_click(self, btn, rows, columns):
        self.game.click(btn, rows, columns)
        print(f"Pressed:[{rows}][{columns}] with {btn}")
        self.refreshBoard()
        if self.game.isGameWon():
            messagebox.showinfo("","You won")


def main():
    gui = Gui()
    gui.mainloop()
        

###################################################


if __name__ =="__main__":
    main()