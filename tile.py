#!/usr/bin/env python3
from enum import Enum, auto

class Tile(Enum):
    EMPTY = auto()
    BLOCK = auto()
    LIGHT = auto()
    BADLIGHT = auto()
    LIT = auto()
    NOLIGHT = auto()
    LITNOLIGHT = auto()
    ZERO = auto()
    BADZERO = auto()
    ONE = auto()
    BADONE = auto()
    TWO = auto()
    BADTWO = auto()
    THREE = auto()
    BADTHREE = auto()
    FOUR = auto()
    BADFOUR = auto()

def main():
    print(list(Tile))    
    

###################################################


if __name__ =="__main__":
    main()