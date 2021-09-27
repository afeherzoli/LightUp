#!/usr/bin/env python3
from square import Square as Sqr
import logging, sys



class Game:
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    grid =  [[Sqr.EMPTY, Sqr.EMPTY, Sqr.ZERO, Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY],
             [Sqr.EMPTY, Sqr.BLOCK, Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY, Sqr.TWO, Sqr.EMPTY],
             [Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY, Sqr.THREE, Sqr.EMPTY, Sqr.EMPTY, Sqr.BLOCK],
             [Sqr.EMPTY, Sqr.EMPTY, Sqr.BLOCK, Sqr.EMPTY, Sqr.TWO, Sqr.EMPTY, Sqr.EMPTY],
             [Sqr.BLOCK, Sqr.EMPTY, Sqr.EMPTY, Sqr.ONE, Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY],
             [Sqr.EMPTY, Sqr.THREE, Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY, Sqr.BLOCK, Sqr.EMPTY],
             [Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY, Sqr.EMPTY, Sqr.ZERO, Sqr.EMPTY, Sqr.EMPTY]]


    def out(self):
        print('x\y 0   1   2   3   4   5   6')
        print(' ',' ---' * 7)
        a = 0
        for i in self.grid:
            print(a,end=' ')
            a += 1
            for j in i:
                print('|', end='')
                
                if j == Sqr.EMPTY:
                    print('  ', end=" ")
                elif j == Sqr.BLOCK:
                    print(' ■', end=" ")
                elif j == Sqr.FOUR:
                    print(' 4', end=" ")
                elif j == Sqr.THREE:
                    print(' 3', end=" ")
                elif j == Sqr.TWO:
                    print(' 2', end=" ")
                elif j == Sqr.ONE:
                    print(' 1', end=" ")
                elif j == Sqr.ZERO:
                    print(' 0', end=" ")
                elif j == Sqr.LIGHT:
                    print(' ¤', end=" ")
                elif j == Sqr.LIT:
                    print(' .', end=" ")
                elif j == Sqr.NOLIGHT:
                    print(' x', end=" ")
            print('|\n  ', '--- '*7)
            
        
    def click(self, btn, row, column):
        btn = int(btn)
        row = int(row)
        column = int(column)

        if btn == 1:
            #left click
            if self.grid[row][column] == Sqr.EMPTY:
                self.__placeLight(row, column)
            elif self.grid[row][column] == Sqr.LIGHT:
                self.__removeLight(row, column)
        elif btn == 3:
            #right click
            if self.grid[row][column] in [Sqr.EMPTY, Sqr.LIT]:
                self.__placeNoLight(row, column)
            elif self.grid[row][column] in [Sqr.NOLIGHT, Sqr.LITNOLIGHT]:
                self.__removeNoLight(row, column)
        else:
            pass
        
    
    def __placeLight(self, row, column):
        row = int(row)
        column = int(column)
        self.grid[row][column] = Sqr.LIGHT
        baseRow = row
        baseColumn = column
        
        row -= 1
        while(0<=row<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] in [Sqr.EMPTY, Sqr.LIT]:
                self.grid[row][column] = Sqr.LIT
            elif self.grid[row][column] in [Sqr.NOLIGHT, Sqr.LITNOLIGHT]:
                self.grid[row][column] = Sqr.LITNOLIGHT
            else:
                break
            row -= 1
            
        row = baseRow
        row += 1
        while(0<=row<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] in [Sqr.EMPTY, Sqr.LIT]:
                self.grid[row][column] = Sqr.LIT
            elif self.grid[row][column] in [Sqr.NOLIGHT, Sqr.LITNOLIGHT]:
                self.grid[row][column] = Sqr.LITNOLIGHT
            else:
                break
            row += 1
            
        row = baseRow
        column -= 1
        while(0<=column<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] in [Sqr.EMPTY, Sqr.LIT]:
                self.grid[row][column] = Sqr.LIT
            elif self.grid[row][column] in [Sqr.NOLIGHT, Sqr.LITNOLIGHT]:
                self.grid[row][column] = Sqr.LITNOLIGHT
            else:
                break
            column -= 1
        
        column = baseColumn
        column += 1
        while(0<=column<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] in [Sqr.EMPTY, Sqr.LIT]:
                self.grid[row][column] = Sqr.LIT
            elif self.grid[row][column] in [Sqr.NOLIGHT, Sqr.LITNOLIGHT]:
                self.grid[row][column] = Sqr.LITNOLIGHT
            else:
                break
            column += 1


    def __removeLight(self, row, column):
        row = int(row)
        column = int(column)
        self.grid[row][column] = Sqr.EMPTY
        baseRow = row
        baseColumn = column
        
        row -= 1
        while(0<=row<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] == Sqr.LIT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.EMPTY
            elif self.grid[row][column] == Sqr.LITNOLIGHT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.NOLIGHT
            row -= 1
            
        row = baseRow
        row += 1
        while(0<=row<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] == Sqr.LIT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.EMPTY
            elif self.grid[row][column] == Sqr.LITNOLIGHT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.NOLIGHT
            row += 1
            
        row = baseRow
        column -= 1
        while(0<=column<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] == Sqr.LIT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.EMPTY
            elif self.grid[row][column] == Sqr.LITNOLIGHT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.NOLIGHT
            column -= 1
        
        column = baseColumn
        column += 1
        while(0<=column<=6 and self.grid[row][column] not in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK, Sqr.LIGHT]):
            if self.grid[row][column] == Sqr.LIT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.EMPTY
            elif self.grid[row][column] == Sqr.LITNOLIGHT:
                if not self.__isLocationLit(row, column):
                    self.grid[row][column] = Sqr.NOLIGHT
            column += 1
    

    def __placeNoLight(self, row, column):
        row = int(row)
        column = int(column)
        if self.__isLocationLit(row, column):
            self.grid[row][column] = Sqr.LITNOLIGHT
        else:
            self.grid[row][column] = Sqr.NOLIGHT


    def __removeNoLight(self, row, column):
        row = int(row)
        column = int(column)

        if self.__isLocationLit(row, column):
            self.grid[row][column] = Sqr.LIT
        else:
            self.grid[row][column] = Sqr.EMPTY
    

    def __isLocationLit(self, row, column):
        row = int(row)
        column = int(column)
        baseRow = row
        baseColumn = column
        
        row -= 1
        while(0<=row<=6):
            if self.grid[row][column] == Sqr.LIGHT:
                return True
            elif self.grid[row][column] in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK]:
                break
            row -= 1
            
        row = baseRow
        row += 1
        while(0<=row<=6):
            if self.grid[row][column] == Sqr.LIGHT:
                return True
            elif self.grid[row][column] in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK]:
                break
            row += 1
            
        row = baseRow
        column -= 1
        while(0<=column<=6):
            if self.grid[row][column] == Sqr.LIGHT:
                return True
            elif self.grid[row][column] in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK]:
                break
            column -= 1
        
        column = baseColumn
        column += 1
        while(0<=column<=6):
            if self.grid[row][column] == Sqr.LIGHT:
                return True
            elif self.grid[row][column] in [Sqr.ZERO, Sqr.ONE, Sqr.TWO, Sqr.THREE, Sqr.FOUR, Sqr.BLOCK]:
                break
            column += 1
        
        return False


    def __todo():
        pass

    def isGameWon(self):
        for rows in range(7):
            for columns in range(7):
                if self.grid[rows][columns] == Sqr.EMPTY:
                    return False
        return True
            
            
        
def main():
    game = Game()   
    

###################################################


if __name__ =="__main__":
    main()
