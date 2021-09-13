#!/usr/bin/env python3
from enum import Enum, auto

class Square(Enum):
    EMPTY = auto()
    BLOCK = auto()
    LIGHT = auto()
    LIT = auto()
    NOLIGHT = auto()
    ZERO = auto()
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()

def main():
    print(list(Square))    
    

###################################################


if __name__ =="__main__":
    main()