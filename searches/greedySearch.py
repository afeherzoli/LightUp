from copy import deepcopy
from operator import itemgetter
from tkinter.constants import FALSE
from square import Square as Sqr
from game import Game
from gui import Gui
from searches.heuristics.simpleHeuristic import simpleHeuristic

           

class GreedySearch():

    def __init__(self, game):
        self.game = game
        self.closed = set()
        self.open = []


    def search(self):
        self.open.append((self.game, simpleHeuristic(self.game)))

        while self.open:
            current, h = self.open.pop(0)
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