#!/usr/bin/env python3
from game import Game
from gui import Gui
from searches.breadth import BreadthFirstSearch
from searches.depth import DepthFirstSearch
from datetime import datetime

def main():
    game = Game(20)
    bfs = BreadthFirstSearch()
    #dfs = DepthFirstSearch()
    print("Started at:", datetime.now().strftime("%H:%M:%S"))
    solved = bfs.search(game)
    print("Finnished at:", datetime.now().strftime("%H:%M:%S"))
    print("Visited positions:", len(bfs.visited))
    gui = Gui(solved)
    gui.start()

###################################################


if __name__ =="__main__":
    main()