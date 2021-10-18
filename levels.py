#!/usr/bin/env python3
from square import Square as Sqr
import random
import xml.etree.ElementTree as ET

def getLevel(num = random.randint(0, 4)):
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

    tree = ET.parse('levels.xml')
    root = tree.getroot()
    myLevel = [[''] * 7 for i in range(7)]

    lvl = root.find('./level[@diff="60"]')

    for row in range(7):
        for col in range(7):
            myLevel[row][col] = textToSqr[root[num][row][col].text]
    return myLevel


def main():
    lvl = getLevel()
    print(lvl)
    

###################################################


if __name__ =="__main__":
    main()