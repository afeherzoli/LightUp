from square import Square as Sqr
from game import Game

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

def secondHeuristic(game):
    heurOfSqrs = [[0] * game.size for i in range(game.size)]

    #first fill the number adjacents
    for rows in range(game.size):
        for columns in range(game.size):
            if game.board[rows][columns] in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
                game.numOfLightsAround
    return sum

def calculate(game, row, column):
    baseRow = row
    baseColumn = column
    vertical = 1.0
    horizontal = 1.0
    
    row -= 1
    while(0 <= row):
        if game.board[row][column] == Sqr.EMPTY:
            horizontal += 1
        row -= 1
        
    row = baseRow
    row += 1
    while(row < self.game.size):
        if game.board[row][column] == Sqr.EMPTY:
            horizontal += 1
        row += 1
        
    row = baseRow
    column -= 1
    while(0 <= column):
        if game.board[row][column] == Sqr.EMPTY:
            vertical += 1
        column -= 1
    
    column = baseColumn
    column += 1
    while(column < self.game.size):
        if game.board[row][column] == Sqr.EMPTY:
            vertical += 1
        column += 1
    
    return 1 / max(horizontal, vertical)

def neighbouringNumber(game, row, column):
    hValue = 0.0

    if not isNeighbourOfNumber(game, row, column):
        return hValue

    if not row==0:
         hValue
        
    
    if not row==game.size-1 and game.board[row+1][column] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
        return hValue
    if not column==0 and game.board[row][column-1] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
        return hValue
    if not column==game.size-1 and game.board[row][column+1] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
        return hValue

    if game[row][column]:
        return 0
    
def isNeighbourOfNumber(game, row, column):
    if not row==0:
        if game.board[row-1][column] not in [Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR]:
            return 

