from copy import deepcopy
from square import Square as Sqr
from game import Game
           
class BreadthFirstSearch():    

    def __init__(self, game):
        self.game = game
        self.closed = set()
        self.open = []


    def search(self):
        self.open.append(self.game)

        while self.open:
            current = self.open.pop(0)
            if current not in self.closed:
                self.closed.add(current)
                if current.isGameWon():
                    return current
                if current.isBoardStateLegit():
                    self.open.extend(self.__successors(current))
        return self.game
        
    def __successors(self, game):
        nexts = []
        for rows in range(7):
            for columns in range(7):
                if game.board[rows][columns] == Sqr.EMPTY:
                    next = deepcopy(game)
                    next.placeLight(rows, columns)
                    nexts.append(next)
        return nexts


def main():
    pass

###################################################


if __name__ =="__main__":
    main()