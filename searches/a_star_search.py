#!/usr/bin/env python3
from tile import Tile as Tile
from game import Game
from gui import Gui
from operator import itemgetter
from copy import deepcopy
           

class AStarSearch():
    __sqrToInt = {
        Tile.ZERO : 0,
        Tile.ONE : 1,
        Tile.TWO  : 2,
        Tile.THREE : 3,
        Tile.FOUR : 4,
        Tile.BADZERO : 0,
        Tile.BADONE : 1,
        Tile.BADTWO  : 2,
        Tile.BADTHREE : 3,
        Tile.BADFOUR : 4,
    }

    def __init__(self, game) -> None:
        self.game = game
        self.visited = set()
        self.queue = []

    def search(self):
        self.queue.append((self.game, self.h1(self.game), 0))

        while self.queue:
            current = self.queue.pop(0)

            if current[0] not in self.visited:
                self.visited.add(current[0])
                if current[0].isGameWon():
                    self.game = current[0]
                    break
                self.queue.extend(self.successors(current[0], current[2]))
                self.queue.sort(key = lambda x: x[1]+x[2])

        
    def h1(self, game):
        # sum of numers - sum of already satisfied numbers
        numbers = 0
        satisfaction = 0
        emptys = 0
        for rows in range(7):
            for columns in range(7):
                if game.board[rows][columns] in [Tile.ZERO, Tile.ONE, Tile.TWO, Tile.THREE, Tile.FOUR]:
                    numbers += self.__sqrToInt[game.board[rows][columns]]
                    satisfaction += self.__numOfLightsAround(game, rows, columns)
        return numbers - satisfaction
    
    def __numOfLightsAround(self, game, row, column):
        lights = 0
        
        if not row==0 and game.board[row-1][column] == Tile.LIGHT:
            lights += 1
        if not row==6 and game.board[row+1][column] == Tile.LIGHT:
            lights += 1
        if not column==0 and game.board[row][column-1] == Tile.LIGHT:
            lights += 1
        if not column==6 and game.board[row][column+1] == Tile.LIGHT:
            lights += 1
        
        return lights

        
    def successors(self, game, cost):
        nexts = []
        for rows in range(7):
            for columns in range(7):
                if game.board[rows][columns] == Tile.EMPTY:
                    next = deepcopy(game)
                    next.click(1, rows, columns)
                    if next.isBoardStateLegit():
                        h = self.h1(next)
                        nexts.append((next, h, cost))
        return nexts


def main():
    pass

###################################################


if __name__ =="__main__":
    main()