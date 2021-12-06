from copy import deepcopy
from operator import itemgetter
from tkinter.constants import FALSE
from square import Square as Sqr
from game import Game
from gui import Gui
from searches.heuristics.simpleHeuristic import simpleHeuristic

           

class GreedyBestFirstSearch():

    def __init__(self, game):
        self.game = game
        self.closed = set()
        self.open = []


    def search(self):
        self.open.append((self.game, simpleHeuristic(self.game)))

        while self.open:
            current, h2 = self.open.pop(0)
            #print(h2)
            #gui = Gui(current)
            #gui.start()

            if current not in self.closed:
                self.closed.add(current)
                if current.isGameWon():
                    return current
                self.open.extend(self.successors(current))
                self.open.sort(key=itemgetter(1))
        return self.game
    
    

    def h2(self, game):
        sum = [[0] * game.size for i in range(game.size)]

        for rows in range(game.size):
            for columns in range(game.size):
                if game.board[rows][columns] == Sqr.EMPTY:
                    sum[rows][columns] = max(self.calculate(game, rows, columns), self.neighbouringNumber(game, rows, columns))
        return sum
    
    def calculate(self, game, row, column):
        baseRow = row
        baseColumn = column
        vertical = 1.0
        horizontal = 1.0
        
        row -= 1
        while(0 <= row):
            if game.board[row][column] == Sqr.EMPTY:
                horizontal += 1
            row -= 1
            
        row = baseRow
        row += 1
        while(row < self.game.size):
            if game.board[row][column] == Sqr.EMPTY:
                horizontal += 1
            row += 1
            
        row = baseRow
        column -= 1
        while(0 <= column):
            if game.board[row][column] == Sqr.EMPTY:
                vertical += 1
            column -= 1
        
        column = baseColumn
        column += 1
        while(column < self.game.size):
            if game.board[row][column] == Sqr.EMPTY:
                vertical += 1
            column += 1
        
        return 1 / max(horizontal, vertical)
    
    def neighbouringNumber(self, game, row, column):
        hValue = 0.0

        if not row==0:
            if game.board[row-1][column] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
                return hValue
            
        
        if not row==game.size-1 and game.board[row+1][column] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
            return hValue
        if not column==0 and game.board[row][column-1] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
            return hValue
        if not column==game.size-1 and game.board[row][column+1] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
            return hValue

        if game[row][column]:
            return 0
        


    

        
    def successors(self, game):
        nexts = []
        for rows in range(game.size):
            for columns in range(game.size):
                if game.board[rows][columns] == Sqr.EMPTY:
                    next = deepcopy(game)
                    next.placeLight(rows, columns)
                    if next.isBoardStateLegit():
                        h = simpleHeuristic(next)
                        nexts.append((next, h))
        return nexts


def main():
    pass

###################################################


if __name__ =="__main__":
    main()