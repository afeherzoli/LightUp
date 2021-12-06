import xml.etree.ElementTree as ET
from square import Square as Sqr


def getLevel(id):
    lvlId = str(id)    
    codeToSqr = {
        'B' : Sqr.BLOCK,
        '0' : Sqr.ZERO,
        '1' : Sqr.ONE,
        '2' : Sqr.TWO,
        '3' : Sqr.THREE,
        '4' : Sqr.FOUR}

    tree = ET.parse('data/finalLevels.xml')
    root = tree.getroot()
    lvl = root.find(f'./level[@id="{lvlId}"]')
    SIZE = int(lvl.attrib['size'])
    
    preLevel = []
    for c in lvl.text:
        if c in ['B', '0', '1', '2', '3', '4']:
            preLevel.append(codeToSqr[c])
        elif ord(c) in range(ord('a'), ord('z')+1):
            preLevel += ([Sqr.EMPTY] * (ord(c)-ord('a')+1))

    myLevel = [[''] * SIZE  for i in range(SIZE)]
    for row in range(SIZE):
        for col in range(SIZE):
            myLevel[row][col] = preLevel[row*SIZE + col]

    return myLevel


def main():
    lvl = getLevel(101)
    print(lvl)
    

###################################################


if __name__ =="__main__":
    main()