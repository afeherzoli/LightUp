#!/usr/bin/env python3
from square import Square as Sqr
from game import Game
from copy import deepcopy
           

class DepthFirstSearch():
    
    visited = set() # List to keep track of visited nodes.
    que = []     #Initialize a queue

    def search(self, game) -> Game:

        self.visited.add(game)
        self.que.extend(self.successors(game))

        while self.que:
            s = self.que.pop()
            if s not in self.visited:
                self.visited.add(s)
                if s.isGameWon():
                    return s
                if s.isWinable():
                    self.que.extend(self.successors(s))
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