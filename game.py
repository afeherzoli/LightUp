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
        print(' --' * 7)
        for i in self.grid:
            for j in i:
                print('|', end='')
                if j == Sqr.EMPTY:
                    print(' ', end=" ")
                elif j == Sqr.BLOCK:
                    print('#', end=" ")
                elif j == Sqr.FOUR:
                    print('4', end=" ")
                elif j == Sqr.THREE:
                    print('3', end=" ")
                elif j == Sqr.TWO:
                    print('2', end=" ")
                elif j == Sqr.ONE:
                    print('1', end=" ")
                elif j == Sqr.ZERO:
                    print('0', end=" ")
                elif j == Sqr.LIGHT:
                    print('*', end=" ")
                elif j == Sqr.LIT:
                    print('.', end=" ")
                elif j == Sqr.NOLIGHT:
                    print('x', end=" ")
            print('|\n', '-- '*7)
        print(self.grid[0][2])

def main():
    game = Game()
    game.out()
    
    
    

###################################################


if __name__ =="__main__":
    main()