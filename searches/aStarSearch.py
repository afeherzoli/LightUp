#!/usr/bin/env python3
from square import Square as Sqr
from game import Game
from gui import Gui
from operator import itemgetter
from copy import deepcopy
           

class AStarSearch():
    __sqrToInt = {
        Sqr.ZERO : 0,
        Sqr.ONE : 1,
        Sqr.TWO  : 2,
        Sqr.THREE : 3,
        Sqr.FOUR : 4,
        Sqr.BADZERO : 0,
        Sqr.BADONE : 1,
        Sqr.BADTWO  : 2,
        Sqr.BADTHREE : 3,
        Sqr.BADFOUR : 4,
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
                if game.board[rows][columns] in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
                    numbers += self.__sqrToInt[game.board[rows][columns]]
                    satisfaction += self.__numOfLightsAround(game, rows, columns)
        return numbers - satisfaction
    
    def __numOfLightsAround(self, game, row, column):
        lights = 0
        
        if not row==0 and game.board[row-1][column] == Sqr.LIGHT:
            lights += 1
        if not row==6 and game.board[row+1][column] == Sqr.LIGHT:
            lights += 1
        if not column==0 and game.board[row][column-1] == Sqr.LIGHT:
            lights += 1
        if not column==6 and game.board[row][column+1] == Sqr.LIGHT:
            lights += 1
        
        return lights

        
    def successors(self, game, cost):
        nexts = []
        for rows in range(7):
            for columns in range(7):
                if game.board[rows][columns] == Sqr.EMPTY:
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