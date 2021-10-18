#!/usr/bin/env python3
from game import Game
from gui import Gui
from breadth import BreadthFirstSearch
from depth import DepthFirstSearch
from datetime import datetime

def main():
    game = Game()
    #bfs = BreadthFirstSearch()
    dfs = DepthFirstSearch()
    print("Started at:", datetime.now().strftime("%H:%M:%S"))
    solved = dfs.search(game)
    print("Finnished at:", datetime.now().strftime("%H:%M:%S"))
    print("Visited positions:", len(dfs.visited))
    gui = Gui(solved)
    gui.start()

###################################################


if __name__ =="__main__":
    main()