#!/usr/bin/env python3
from game import Game
from gui import Gui
from searches.depthFirstSearch import DepthFirstSearch
from searches.depthLimitedSearch import DepthLimitedSearch
from searches.iterativeDeepeningDepthFirstSearch import IterativeDeepeningDepthFirstSearch
from datetime import datetime

def main():
    game = Game(59)
    """ dfs = DepthFirstSearch()
    print("Started at:", datetime.now().strftime("%H:%M:%S"))
    solved = dfs.search(game)
    print("Finnished at:", datetime.now().strftime("%H:%M:%S"))
    print("Visited positions:", len(dfs.visited))
    gui = Gui(solved)
    gui.start() """

    srch = DepthFirstSearch()
    print("Started at:", datetime.now().strftime("%H:%M:%S"))
    solved = srch.search(game)
    print("Finnished at:", datetime.now().strftime("%H:%M:%S"))
    print("Visited positions:", len(srch.visited))

    gui = Gui(solved)
    gui.start()

###################################################


if __name__ =="__main__":
    main()