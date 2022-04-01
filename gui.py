from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, Font, nametofont
from game import Game
from tile import Tile as Tile


class Gui():

    __symbols = {
        Tile.EMPTY : '',
        Tile.BLOCK : ' ',
        Tile.LIGHT : 'O',
        Tile.BADLIGHT : '@',
        Tile.LIT : ' ',
        Tile.NOLIGHT : 'x',
        Tile.LITNOLIGHT : 'x',
        Tile.ZERO : '0',
        Tile.BADZERO : '0',
        Tile.ONE : '1',
        Tile.BADONE : '1',
        Tile.TWO : '2',
        Tile.BADTWO : '2',
        Tile.THREE : '3',
        Tile.BADTHREE : '3',
        Tile.FOUR : '4',
        Tile.BADFOUR : '4'}

    __bgColors = {
        Tile.EMPTY : 'snow3',
        Tile.BLOCK : 'black',
        Tile.LIGHT : 'yellow',
        Tile.BADLIGHT : 'yellow',
        Tile.LIT : 'yellow',
        Tile.NOLIGHT : 'snow3',
        Tile.LITNOLIGHT : 'yellow',
        Tile.ZERO : 'black',
        Tile.BADZERO : 'black',
        Tile.ONE : 'black',
        Tile.BADONE : 'black',
        Tile.TWO : 'black',
        Tile.BADTWO : 'black',
        Tile.THREE : 'black',
        Tile.BADTHREE : 'black',
        Tile.FOUR : 'black',
        Tile.BADFOUR : 'black'}

    __fgColors = {
        Tile.EMPTY : 'white',
        Tile.BLOCK : 'black',
        Tile.LIGHT : 'black',
        Tile.BADLIGHT : 'red',
        Tile.LIT : 'yellow',
        Tile.NOLIGHT : 'black',
        Tile.LITNOLIGHT : 'black',
        Tile.ZERO : 'white',
        Tile.BADZERO : 'red',
        Tile.ONE : 'white',
        Tile.BADONE : 'red',
        Tile.TWO : 'white',
        Tile.BADTWO : 'red',
        Tile.THREE : 'white',
        Tile.BADTHREE : 'red',
        Tile.FOUR : 'white',
        Tile.BADFOUR : 'red'}

    def __init__(self, game):
        self.game = game
        self.is_game_already_won = False
        self.root = Tk()
        self.root.title("Light Up")
        self.root.configure(background="snow4")
        self.root.geometry("364x392")
        self.root.minsize(36 * self.game.size, 38 * self.game.size)
        self.root.maxsize(36 * self.game.size, 38 * self.game.size)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        my_font = nametofont("TkDefaultFont")
        my_font.configure(weight='bold')
        self.root.option_add("*Font", my_font)
        self.__initialzie_board()


    def start(self):
        self.root.mainloop()


    def __initialzie_board(self):
        for rows in range(self.game.size):
            for columns in range(self.game.size):
                lbl = Label(self.root, height=2, width=4, fg="black", bg="gray")
                lbl.grid(row=rows, column=columns, padx=(1, 1), pady=(1,1))
                lbl['text'] = self.__get_symbol_at(rows, columns)
                lbl['bg'] = self.__get_bg_at(rows, columns)
                lbl['fg'] = self.__get_fg_at(rows, columns)
                if self.game.board[rows][columns] not in [
                    Tile.ZERO, Tile.ONE, Tile.TWO, Tile.THREE, Tile.FOUR, Tile.BLOCK,
                    Tile.BADZERO, Tile.BADONE, Tile.BADTWO, Tile.BADTHREE, Tile.BADFOUR]:
                    lbl.bind("<Button-1>", lambda e, x=rows, y=columns: self.button_click(1, x, y))
                    lbl.bind("<Button-3>", lambda e, x=rows, y=columns: self.button_click(3, x, y))
        if self.is_game_already_won==False and self.game.is_game_won():
            self.is_game_already_won = True
                
    
    def __refresh_board(self):
        for rows in range(self.game.size):
            for columns in range(self.game.size):
                widget = self.root.grid_slaves(row=rows, column=columns)[0]
                widget['text'] = self.__get_symbol_at(rows, columns)
                widget['bg'] = self.__get_bg_at(rows, columns)
                widget['fg'] = self.__get_fg_at(rows, columns)


    def __get_symbol_at(self, row, column):
        return self.__symbols[self.game.board[row][column]]


    def __get_bg_at(self, row, column):
        return self.__bgColors[self.game.board[row][column]]


    def __get_fg_at(self, row, column):
        return self.__fgColors[self.game.board[row][column]]


    def button_click(self, btn, row, column):
        if btn == 1:
            self.game.place_light(row, column)
        elif btn == 3:
            self.game.place_no_light(row, column)

        self.__refresh_board()
        if self.is_game_already_won==False and self.game.is_game_won():
            self.is_game_already_won = True
            messagebox.showinfo("","You won")


def main():
    game = Game(23)
    gui = Gui(game)
    gui.start()
        

###################################################


if __name__ =="__main__":
    main()