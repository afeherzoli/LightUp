#!/usr/bin/env python3
from square import Square as Sqr

class Game:
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
                    print(' #', end=" ")
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
            
        
    def click(self, line, row, mouse):
        line = int(line)
        row = int(row)
        mouse = int(mouse)
        if self.grid[line][row] in [Sqr.EMPTY, Sqr.LIGHT, Sqr.NOLIGHT]:
            self.placeLigth(line, row)
        
    
    def placeLigth(self, line, row):
        self.grid[line][row] = Sqr.LIGHT
        baseLine = line
        baseRow = row
        
        line -= 1
        while(0<=line<=6 and self.grid[line][row] in [Sqr.EMPTY, Sqr.LIT]):
            self.grid[line][row] = Sqr.LIT
            line -= 1
            
        line = baseLine
        line += 1
        while(0<=line<=6 and self.grid[line][row] in [Sqr.EMPTY, Sqr.LIT]):
            self.grid[line][row] = Sqr.LIT
            line += 1
            
        line = baseLine
        row -= 1
        while(0<=row<=6 and self.grid[line][row] in [Sqr.EMPTY, Sqr.LIT]):
            self.grid[line][row] = Sqr.LIT
            row -= 1
        
        row = baseRow
        row += 1
        while(0<=row<=6 and self.grid[line][row] in [Sqr.EMPTY, Sqr.LIT]):
            self.grid[line][row] = Sqr.LIT
            row += 1
            
            
        
def main():
    game = Game()
    game.out()
    while True:
        print('Mit lépsz?')
        x = input('x: ')
        y = input('y: ')
        clk = input('0/1: ')
        game.click(x, y, 0)
        game.out()
    
    
    

###################################################


if __name__ =="__main__":
    main()