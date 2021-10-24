#!/usr/bin/env python3
from square import Square as Sqr
import xml.etree.ElementTree as ET

def getLevel(id):    
    codeToSqr = {
        'B' : Sqr.BLOCK,
        '0' : Sqr.ZERO,
        '1' : Sqr.ONE,
        '2' : Sqr.TWO,
        '3' : Sqr.THREE,
        '4' : Sqr.FOUR}

    tree = ET.parse('data/levels.xml')
    root = tree.getroot()
    myLevel = [[''] * 7 for i in range(7)]
    preLevel = []

    lvl = root.find(f'./level[@id="{id}"]')

    print(f"loading level with id:{id}")

    for c in lvl.text:
        if c in ['B', '0', '1', '2', '3', '4']:
            preLevel.append(codeToSqr[c])
        elif ord(c) in range(ord('a'), ord('z')+1):
            preLevel += ([Sqr.EMPTY] * (ord(c)-ord('a')+1))

    for row in range(7):
        for col in range(7):
            myLevel[row][col] = preLevel[row*7 + col]

    return myLevel


def main():
    lvl = getLevel()
    print(lvl)
    

###################################################


if __name__ =="__main__":
    main()