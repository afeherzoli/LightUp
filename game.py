#!/usr/bin/env python3
from square import Square as Sqr
from getLevel import getLevel
import logging, sys


class Game:
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    def __init__(self, lvlId):
        self.board = getLevel(id= str(lvlId))

    def __hash__(self):
        return hash(str(self.board))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.board == other.board

    __changeIfLit = {
        Sqr.EMPTY : Sqr.LIT,
        Sqr.LIGHT : Sqr.BADLIGHT,
        Sqr.BADLIGHT : Sqr.BADLIGHT,
        Sqr.LIT : Sqr.LIT,
        Sqr.NOLIGHT : Sqr.LITNOLIGHT,
        Sqr.LITNOLIGHT : Sqr.LITNOLIGHT}

    __changeIfNotLit = {
        Sqr.EMPTY : Sqr.EMPTY,
        Sqr.LIGHT : Sqr.LIGHT,
        Sqr.BADLIGHT : Sqr.LIGHT,
        Sqr.LIT : Sqr.EMPTY,
        Sqr.NOLIGHT : Sqr.NOLIGHT,
        Sqr.LITNOLIGHT : Sqr.NOLIGHT}

    __changeIfCanSatisfy ={
        Sqr.ZERO : Sqr.ZERO,
        Sqr.BADZERO : Sqr.ZERO,
        Sqr.ONE : Sqr.ONE,
        Sqr.BADONE : Sqr.ONE,
        Sqr.TWO : Sqr.TWO,
        Sqr.BADTWO : Sqr.TWO,
        Sqr.THREE : Sqr.THREE,
        Sqr.BADTHREE : Sqr.THREE,
        Sqr.FOUR : Sqr.FOUR,
        Sqr.BADFOUR : Sqr.FOUR,
        Sqr.BLOCK : Sqr.BLOCK}

    __changeIfCanNotSatisfy ={
        Sqr.ZERO : Sqr.BADZERO,
        Sqr.BADZERO : Sqr.BADZERO,
        Sqr.ONE : Sqr.BADONE,
        Sqr.BADONE : Sqr.BADONE,
        Sqr.TWO : Sqr.BADTWO,
        Sqr.BADTWO : Sqr.BADTWO,
        Sqr.THREE : Sqr.BADTHREE,
        Sqr.BADTHREE : Sqr.BADTHREE,
        Sqr.FOUR : Sqr.BADFOUR,
        Sqr.BADFOUR : Sqr.BADFOUR,
        Sqr.BLOCK : Sqr.BLOCK
    }
      
    def click(self, btn, row, column):
        #print(f"click [{row}][{column}] with {btn}")
        btn = int(btn)
        row = int(row)
        column = int(column)

        if btn == 1:
            #left click
            if self.board[row][column] in [Sqr.EMPTY, Sqr.LIT]:
                self.__placeLight(row, column)
            elif self.board[row][column] in [Sqr.LIGHT, Sqr.BADLIGHT]:
                self.__removeLight(row, column)
        elif btn == 3:
            #right click
            if self.board[row][column] in [Sqr.EMPTY, Sqr.LIT]:
                self.__placeNoLight(row, column)
            elif self.board[row][column] in [Sqr.NOLIGHT, Sqr.LITNOLIGHT]:
                self.__removeNoLight(row, column)
        else:
            pass
        self.__refreshGrid()
        
    
    def __placeLight(self, row, column):
        row = int(row)
        column = int(column)
        self.board[row][column] = Sqr.LIGHT


    def __removeLight(self, row, column):
        row = int(row)
        column = int(column)
        self.board[row][column] = Sqr.EMPTY
    

    def __placeNoLight(self, row, column):
        row = int(row)
        column = int(column)
        if self.__isLocationLit(row, column):
            self.board[row][column] = Sqr.LITNOLIGHT
        else:
            self.board[row][column] = Sqr.NOLIGHT


    def __removeNoLight(self, row, column):
        row = int(row)
        column = int(column)

        if self.__isLocationLit(row, column):
            self.board[row][column] = Sqr.LIT
        else:
            self.board[row][column] = Sqr.EMPTY
    

    def __isLocationLit(self, row, column):
        row = int(row)
        column = int(column)
        baseRow = row
        baseColumn = column
        
        row -= 1
        while(0<=row<=6):
            if self.board[row][column] in [Sqr.LIGHT, Sqr.BADLIGHT]:
                return True
            elif self.__isLocationStopsLight(row, column):
                break
            row -= 1
            
        row = baseRow
        row += 1
        while(0<=row<=6):
            if self.board[row][column] in [Sqr.LIGHT, Sqr.BADLIGHT]:
                return True
            elif self.__isLocationStopsLight(row, column):
                break
            row += 1
            
        row = baseRow
        column -= 1
        while(0<=column<=6):
            if self.board[row][column] in [Sqr.LIGHT, Sqr.BADLIGHT]:
                return True
            elif self.__isLocationStopsLight(row, column):
                break
            column -= 1
        
        column = baseColumn
        column += 1
        while(0<=column<=6):
            if self.board[row][column] in [Sqr.LIGHT, Sqr.BADLIGHT]:
                return True
            elif self.__isLocationStopsLight(row, column):
                break
            column += 1
        
        return False


    def __isLocationStopsLight(self, row, column):
        row = int(row)
        column = int(column)
        if self.board[row][column] in [
            Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK,
            Sqr.BADZERO, Sqr.BADONE, Sqr.BADTWO, Sqr.BADTHREE, Sqr.BADFOUR
            ]:
                return True
        else:
            return False


    def __isLocationChangedByLight(self, row, column):
        if self.board[row][column] in [Sqr.EMPTY, Sqr.LIGHT, Sqr.BADLIGHT, Sqr.LIT, Sqr.NOLIGHT, Sqr.LITNOLIGHT]:
            return True
        return False
    

    def __canSatisfy(self, row, column):
        #logging.debug(f'_canSatisfy({row}, {column})')
        if self.board[row][column] in [Sqr.ZERO, Sqr.BADZERO]:
            if self.__numOfLightsAround(row, column) == 0:
                return True
            elif self.__numOfLightsAround(row, column) > 0:
                return False
            elif self.__numOfLightsAround(row, column) + self.__numOfEmptyAround(row, column) >= 0:
                return True
        elif self.board[row][column] in [Sqr.ONE, Sqr.BADONE]:
            if self.__numOfLightsAround(row, column) == 1:
                return True
            elif self.__numOfLightsAround(row, column) > 1:
                return False
            elif self.__numOfLightsAround(row, column) + self.__numOfEmptyAround(row, column) >= 1:
                return True
        elif self.board[row][column] in [Sqr.TWO, Sqr.BADTWO]:
            if self.__numOfLightsAround(row, column) == 2:
                return True
            elif self.__numOfLightsAround(row, column) > 2:
                return False
            elif self.__numOfLightsAround(row, column) + self.__numOfEmptyAround(row, column) >= 2:
                return True
        elif self.board[row][column] in [Sqr.THREE, Sqr.BADTHREE]:
            if self.__numOfLightsAround(row, column) == 3:
                return True
            elif self.__numOfLightsAround(row, column) > 3:
                return False
            elif self.__numOfLightsAround(row, column) + self.__numOfEmptyAround(row, column) >= 3:
                return True
        elif self.board[row][column] in [Sqr.FOUR, Sqr.BADFOUR]:
            if self.__numOfLightsAround(row, column) == 4:
                return True
            elif self.__numOfLightsAround(row, column) > 4:
                return False
            elif self.__numOfLightsAround(row, column) + self.__numOfEmptyAround(row, column) >= 4:
                return True
        elif self.board[row][column] in [Sqr.BLOCK]:
            return True
        return False
        
        
    def __numOfLightsAround(self, row, column):
        lights = 0
        
        if not row==0 and self.board[row-1][column] in [Sqr.LIGHT, Sqr.BADLIGHT]:
            lights += 1

        if not row==6 and self.board[row+1][column] in [Sqr.LIGHT, Sqr.BADLIGHT]:
            lights += 1

        if not column==0 and self.board[row][column-1] in [Sqr.LIGHT, Sqr.BADLIGHT]:
            lights += 1

        if not column==6 and self.board[row][column+1] in [Sqr.LIGHT, Sqr.BADLIGHT]:
            lights += 1
        
        return lights
        
    
    def __numOfEmptyAround(self, row, column):
        emptys = 0
        
        if not row==0 and self.board[row-1][column] == Sqr.EMPTY:
            emptys += 1

        if not row==6 and self.board[row+1][column] == Sqr.EMPTY:
            emptys += 1

        if not column==0 and self.board[row][column-1] == Sqr.EMPTY:
            emptys += 1

        if not column==6 and self.board[row][column+1] == Sqr.EMPTY:
            emptys += 1
        
        return emptys


    def __refreshGrid(self):
        for rows in range(7):
            for columns in range(7):
                if self.__isLocationChangedByLight(rows, columns):
                    if self.__isLocationLit(rows, columns):
                        self.board[rows][columns] = self.__changeIfLit[self.board[rows][columns]]
                    else:
                        self.board[rows][columns] = self.__changeIfNotLit[self.board[rows][columns]]
        for rows in range(7):
            for columns in range(7):
                if self.__isLocationStopsLight(rows, columns):
                    if self.__canSatisfy(rows, columns):
                        self.board[rows][columns] = self.__changeIfCanSatisfy[self.board[rows][columns]]
                    else:
                        self.board[rows][columns] = self.__changeIfCanNotSatisfy[self.board[rows][columns]]


    def isGameWon(self):
        for rows in range(7):
            for columns in range(7):
                if self.board[rows][columns] in [
                    Sqr.EMPTY, Sqr.NOLIGHT, Sqr.BADLIGHT, Sqr.BADZERO, Sqr.BADONE, Sqr.BADTWO, Sqr.BADTHREE, Sqr.BADFOUR
                ]:
                    return False
        return True

    def isBoardStateLegit(self):
        for rows in range(7):
            for columns in range(7):
                if self.board[rows][columns] in [
                    Sqr.BADLIGHT, Sqr.BADZERO, Sqr.BADONE, Sqr.BADTWO, Sqr.BADTHREE, Sqr.BADFOUR
                ]:
                    return False
        return True
            
            
        
def main():
    game = Game()   
    

###################################################


if __name__ =="__main__":
    main()
