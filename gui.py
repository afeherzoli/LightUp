from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, Font, nametofont
from game import Game
from square import Square as Sqr


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
        Sqr.BADFOUR : '4'}

    __bgColors = {
        Sqr.EMPTY : 'snow3',
        Sqr.BLOCK : 'black',
        Sqr.LIGHT : 'yellow',
        Sqr.BADLIGHT : 'yellow',
        Sqr.LIT : 'yellow',
        Sqr.NOLIGHT : 'snow3',
        Sqr.LITNOLIGHT : 'yellow',
        Sqr.ZERO : 'black',
        Sqr.BADZERO : 'black',
        Sqr.ONE : 'black',
        Sqr.BADONE : 'black',
        Sqr.TWO : 'black',
        Sqr.BADTWO : 'black',
        Sqr.THREE : 'black',
        Sqr.BADTHREE : 'black',
        Sqr.FOUR : 'black',
        Sqr.BADFOUR : 'black'}

    __fgColors = {
        Sqr.EMPTY : 'white',
        Sqr.BLOCK : 'black',
        Sqr.LIGHT : 'black',
        Sqr.BADLIGHT : 'red',
        Sqr.LIT : 'yellow',
        Sqr.NOLIGHT : 'black',
        Sqr.LITNOLIGHT : 'black',
        Sqr.ZERO : 'white',
        Sqr.BADZERO : 'red',
        Sqr.ONE : 'white',
        Sqr.BADONE : 'red',
        Sqr.TWO : 'white',
        Sqr.BADTWO : 'red',
        Sqr.THREE : 'white',
        Sqr.BADTHREE : 'red',
        Sqr.FOUR : 'white',
        Sqr.BADFOUR : 'red'}

    def __init__(self, game):
        self.game = game
        self.isGameAlreadyWon = False
        self.root = Tk()
        self.root.title("Light Up")
        self.root.configure(background="snow4")
        self.root.geometry("364x392")
        self.root.minsize(36 * self.game.size, 38 * self.game.size)
        self.root.maxsize(36 * self.game.size, 38 * self.game.size)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        myFont = nametofont("TkDefaultFont")
        myFont.configure(weight='bold')
        self.root.option_add("*Font", myFont)
        self.__initialzieBoard()


    def start(self):
        self.root.mainloop()


    def __initialzieBoard(self):
        for rows in range(self.game.size):
            for columns in range(self.game.size):
                lbl = Label(self.root, height=2, width=4, fg="black", bg="gray")
                lbl.grid(row=rows, column=columns, padx=(1, 1), pady=(1,1))
                lbl['text'] = self.__getSymbolAt(rows, columns)
                lbl['bg'] = self.__getBgAt(rows, columns)
                lbl['fg'] = self.__getFgAt(rows, columns)
                if self.game.board[rows][columns] not in [
                    Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK,
                    Sqr.BADZERO, Sqr.BADONE, Sqr.BADTWO, Sqr.BADTHREE, Sqr.BADFOUR]:
                    lbl.bind("<Button-1>", lambda e, x=rows, y=columns: self.buttonClick(1, x, y))
                    lbl.bind("<Button-3>", lambda e, x=rows, y=columns: self.buttonClick(3, x, y))
        if self.isGameAlreadyWon==False and self.game.isGameWon():
            self.isGameAlreadyWon = True
                
    
    def __refreshBoard(self):
        for rows in range(self.game.size):
            for columns in range(self.game.size):
                widget = self.root.grid_slaves(row=rows, column=columns)[0]
                widget['text'] = self.__getSymbolAt(rows, columns)
                widget['bg'] = self.__getBgAt(rows, columns)
                widget['fg'] = self.__getFgAt(rows, columns)


    def __getSymbolAt(self, row, column):
        return self.__symbols[self.game.board[row][column]]


    def __getBgAt(self, row, column):
        return self.__bgColors[self.game.board[row][column]]


    def __getFgAt(self, row, column):
        return self.__fgColors[self.game.board[row][column]]


    def buttonClick(self, btn, row, column):
        if btn == 1:
            self.game.placeLight(row, column)
        elif btn == 3:
            self.game.placeNoLight(row, column)

        self.__refreshBoard()
        if self.isGameAlreadyWon==False and self.game.isGameWon():
            self.isGameAlreadyWon = True
            messagebox.showinfo("","You won")


def main():
    game = Game(1)
    gui = Gui(game)
    gui.start()
        

###################################################


if __name__ =="__main__":
    main()