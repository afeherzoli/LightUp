from datetime import datetime
from game import Game
from gui import Gui
from searches.breadthFirstSearch import BreadthFirstSearch
from searches.depthFirstSearch import DepthFirstSearch
from searches.depthLimitedSearch import DepthLimitedSearch
from searches.iterativeDeepeningDepthFirstSearch import IterativeDeepeningDepthFirstSearch
from searches.greedySearch import GreedySearch
from searches.aStarSearch import AStarSearch


def main():
    for i in range(15, 28):
        
        #f = open("data/breadth_results.txt", "a")
        
        #i = 36 # game id, 0-59
        game = Game(i)

        print(f"Solving game with id:{i}")
        mySearch = GreedySearch(game)
        startTime  = datetime.now()
        #f.write(str(i)+'|')
        solved = mySearch.search()
        #f.write(str((datetime.now()-startTime).total_seconds()) + '|')
        space = len(mySearch.open) + len(mySearch.closed)
        print("runtime:",(datetime.now()-startTime).total_seconds(), "| size:", space)
        #f.write(str(space) + '\n')
        gui = Gui(solved)
        gui.start()
        #f.close()

###################################################


if __name__ =="__main__":
    main()
