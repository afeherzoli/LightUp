from square import Square as Sqr

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


def simpleHeuristic(game):
        # sum of numers - sum of already satisfied numbers
        numbers = 0
        satisfaction = 0
        for rows in range(game.size):
            for columns in range(game.size):
                if game.board[rows][columns] in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
                    numbers += __sqrToInt[game.board[rows][columns]]
                    satisfaction += __numOfLightsAround(game, rows, columns)
        return numbers - satisfaction

def __numOfLightsAround(game, row, column):
        lights = 0
        
        if not row==0 and game.board[row-1][column] == Sqr.LIGHT:
            lights += 1
        if not row==game.size-1 and game.board[row+1][column] == Sqr.LIGHT:
            lights += 1
        if not column==0 and game.board[row][column-1] == Sqr.LIGHT:
            lights += 1
        if not column==game.size-1 and game.board[row][column+1] == Sqr.LIGHT:
            lights += 1
        
        return lights