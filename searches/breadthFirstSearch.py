#!/usr/bin/env python3
from square import Square as Sqr
from game import Game
from copy import deepcopy
           

class BreadthFirstSearch():    
    visited = set()
    queue = []

    def search(self, game) -> Game:
        self.queue.append(game)

        while self.queue:
            current = self.queue.pop(0)
            if current not in self.visited:
                self.visited.add(current)
                if current.isGameWon():
                    return current
                if current.isBoardStateLegit():
                    self.queue.extend(self.successors(current))
        return game
        
    
    def successors(self, game):
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