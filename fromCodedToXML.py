#!/usr/bin/env python3

def xmlToBoard():
    writeFile = open("./data/levels.xml", "w")
    readFile = open("./data/coded", "r")

    writeFile.write('<?xml version="1.0"?>\n')
    writeFile.write("<levels>\n")

    for line in readFile:
        if line == "":
            break
        id = line.strip().split(":")[0]
        code = line.strip().split(":")[1]
        writeFile.write(f'   <level id="{id}">{code}</level>\n')

    writeFile.write("</levels>")

    readFile.close()
    writeFile.close()


def main():
    xmlToBoard()
    

###################################################


if __name__ =="__main__":
    main()