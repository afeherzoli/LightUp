#!/usr/bin/env python3
from square import Square as Sqr
import random
import xml.etree.ElementTree as ET

def getLevel():
    textToSqr = {
        'Sqr.EMPTY' : Sqr.EMPTY,
        'Sqr.BLOCK' : Sqr.BLOCK,
        'Sqr.LIGHT' : Sqr.LIGHT,
        'Sqr.BADLIGHT' : Sqr.BADLIGHT,
        'Sqr.LIT' : Sqr.LIT,
        'Sqr.NOLIGHT' : Sqr.NOLIGHT,
        'Sqr.LITNOLIGHT' : Sqr.LITNOLIGHT,
        'Sqr.ZERO' : Sqr.ZERO,
        'Sqr.BADZERO' : Sqr.BADZERO,
        'Sqr.ONE' : Sqr.ONE,
        'Sqr.BADONE' : Sqr.BADONE,
        'Sqr.TWO' : Sqr.TWO,
        'Sqr.BADTWO' : Sqr.BADTWO,
        'Sqr.THREE' : Sqr.THREE,
        'Sqr.BADTHREE' : Sqr.BADTHREE,
        'Sqr.FOUR' : Sqr.FOUR,
        'Sqr.BADFOUR' : Sqr.BADFOUR}

    writeFile = open("saves/coded.txt", "w")

    for i in range(20, 60):
        readFile = open(f"saves/{i}", "r")
        lineNum = 0
        for line in readFile:
            lineNum += 1
            if lineNum == 7:
                code = line.strip().split(":")[-1]
                writeFile.write(f"{i}:"+code+"\n")
        readFile.close()

    writeFile.close()

def main():
    getLevel()
    

###################################################


if __name__ =="__main__":
    main()