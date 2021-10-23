#!/usr/bin/env python3

def getLevel():
    writeFile = open("./data/coded", "w")

    for i in range(20, 60):
        readFile = open(f"./data/saves/{i}", "r")
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