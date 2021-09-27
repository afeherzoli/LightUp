from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, Font, nametofont
from game import Game
from square import Square as Sqr

SIZE = 7

class Gui():

    __symbols = {
        Sqr.EMPTY : '',
        Sqr.BLOCK : ' ',
        Sqr.LIGHT : 'O',
        Sqr.BADLIGHT : '@',
        Sqr.LIT : ' ',
        Sqr.NOLIGHT : 'x',
        Sqr.LITNOLIGHT : 'x',
        Sqr.ZERO : '0',
        Sqr.BADZERO : '0',
        Sqr.ONE : '1',
        Sqr.BADONE : '1',
        Sqr.TWO : '2',
        Sqr.BADTWO : '2',
        Sqr.THREE : '3',
        Sqr.BADTHREE : '3',
        Sqr.FOUR : '4',
        Sqr.BADFOUR : '4',
    }

    __bgColors = {
        Sqr.EMPTY : 'white',
        Sqr.BLOCK : 'black',
        Sqr.LIGHT : 'yellow',
        Sqr.BADLIGHT : 'yellow',
        Sqr.LIT : 'yellow',
        Sqr.NOLIGHT : 'white',
        Sqr.LITNOLIGHT : 'yellow',
        Sqr.ZERO : 'gray',
        Sqr.BADZERO : 'gray',
        Sqr.ONE : 'gray',
        Sqr.BADONE : 'gray',
        Sqr.TWO : 'gray',
        Sqr.BADTWO : 'gray',
        Sqr.THREE : 'gray',
        Sqr.BADTHREE : 'gray',
        Sqr.FOUR : 'gray',
        Sqr.BADFOUR : 'gray',
    }

    __fgColors = {
        Sqr.EMPTY : 'white',
        Sqr.BLOCK : 'black',
        Sqr.LIGHT : 'black',
        Sqr.BADLIGHT : 'red',
        Sqr.LIT : 'yellow',
        Sqr.NOLIGHT : 'black',
        Sqr.LITNOLIGHT : 'black',
        Sqr.ZERO : 'black',
        Sqr.BADZERO : 'red',
        Sqr.ONE : 'black',
        Sqr.BADONE : 'red',
        Sqr.TWO : 'black',
        Sqr.BADTWO : 'red',
        Sqr.THREE : 'black',
        Sqr.BADTHREE : 'red',
        Sqr.FOUR : 'black',
        Sqr.BADFOUR : 'red',
    }


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
        return self.__symbols[self.game.grid[rows][columns]]


    def __bgAt(self, rows, columns):
        return self.__bgColors[self.game.grid[rows][columns]]


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