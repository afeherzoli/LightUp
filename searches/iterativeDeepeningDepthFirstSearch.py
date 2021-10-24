#!/usr/bin/env python3
from square import Square as Sqr
from game import Game
from gui import Gui
from copy import deepcopy


class IterativeDeepeningDepthFirstSearch():
    visited = set()

    def search(self, game, depth) -> Game:
        for i in range(depth):
            self.visited = set()
            result = self.__dls(game, depth=i)
            if result is not None:
                return result
        return game


    def __dls(self, game, depth):
        if depth == 0:
            if game.isGameWon():
                return game
            else:
                return None

        elif depth > 0:
            for node in self.__successors(game):
                self.visited.add(node)                
                if node.isBoardStateLegit() or (node not in self.visited):
                    solved = self.__dls(node, depth-1)
                else:
                    continue                
                if solved is not None:
                    return solved
            return None

    
    def __successors(self, game):
        nexts = []
        for rows in range(7):
            for columns in range(7):
                if game.board[rows][columns] == Sqr.EMPTY:
                    next = deepcopy(game)
                    next.click(1, rows, columns)
                    nexts.append(next)
        return nexts


def main():
    pass
    

###################################################


if __name__ =="__main__":
    main()