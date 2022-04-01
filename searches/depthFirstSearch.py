from copy import deepcopy
from tile import Tile as Tile
from game import Game
         
class DepthFirstSearch():

    def __init__(self, game):
        self.game = game
        self.closed = set()
        self.open = []


    def search(self):
        self.open.append(self.game)

        while self.open:
            current = self.open.pop()
            if current not in self.closed:
                self.closed.add(current)
                if current.isGameWon():
                    self.game = current
                    break
                if current.isBoardStateLegit():
                    self.open.extend(self.successors(current))
        
    
    def successors(self, game):
        nexts = []
        for rows in range(7):
            for columns in range(7):
                if game.board[rows][columns] == Tile.EMPTY:
                    next = deepcopy(game)
                    next.placeLight(rows, columns)
                    nexts.append(next)
        return nexts


def main():
    pass

###################################################


if __name__ =="__main__":
    main()