from datetime import datetime
from game import Game
from gui import Gui
from searches.breadthFirstSearch import BreadthFirstSearch
from searches.depthFirstSearch import DepthFirstSearch
from searches.depthLimitedSearch import DepthLimitedSearch
from searches.iterativeDeepeningDepthFirstSearch import IterativeDeepeningDepthFirstSearch
from searches.greedyBestFirstSearch import GreedyBestFirstSearch
from searches.aStarSearch import AStarSearch


def main():
    for i in range(0, 60):
        print(i)
        #f = open("data/breadth_results.txt", "a")
        #i = 29
        game = Game(i)

        mySearch = GreedyBestFirstSearch(game)
        startTime  = datetime.now()
        #f.write(str(i)+'|')
        solved = mySearch.search()
        size = len(mySearch.open) + len(mySearch.closed)
        #f.write(str((datetime.now()-startTime).total_seconds()) + '|')
        #space = len(mySearch.open) + len(mySearch.closed)
        print("runtime:",(datetime.now()-startTime).total_seconds(), "| size:", size)
        #f.write(str(space) + '\n')
        #gui = Gui(solved)
        #gui.start()
        #f.close()
    #gui = Gui(solved)
    #gui.start()

###################################################


if __name__ =="__main__":
    main()
