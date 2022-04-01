from tile import Tile as Tile

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


def simpleHeuristic(game):
        # sum of numers - sum of already satisfied numbers
        numbers = 0
        satisfaction = 0
        for rows in range(game.size):
            for columns in range(game.size):
                if game.board[rows][columns] in [Tile.ZERO, Tile.ONE, Tile.TWO, Tile.THREE, Tile.FOUR]:
                    numbers += __sqrToInt[game.board[rows][columns]]
                    satisfaction += __numOfLightsAround(game, rows, columns)
        return numbers - satisfaction

def __numOfLightsAround(game, row, column):
        lights = 0
        
        if not row==0 and game.board[row-1][column] == Tile.LIGHT:
            lights += 1
        if not row==game.size-1 and game.board[row+1][column] == Tile.LIGHT:
            lights += 1
        if not column==0 and game.board[row][column-1] == Tile.LIGHT:
            lights += 1
        if not column==game.size-1 and game.board[row][column+1] == Tile.LIGHT:
            lights += 1
        
        return lights