from datetime import datetime
from game import Game
from gui import Gui
from searches.breadthFirstSearch import BreadthFirstSearch
from searches.depthFirstSearch import DepthFirstSearch
from searches.depthLimitedSearch import DepthLimitedSearch
from searches.iterativeDeepeningDepthFirstSearch import IterativeDeepeningDepthFirstSearch
from searches.greedySearch import GreedySearch
from searches.aStarSearch import AStarSearch
from searches.heuristics.preprocess import preprocess


def main():
    for i in range(60):
        
        #f = open("data/breadth_results.txt", "a")
        
        #i = 27 # game id, 0-59
        game = Game(i)
        preprocess(game)

        print(f"Solving game with id:{i}")
        mySearch = GreedySearch(game)
        startTime  = datetime.now()
        #f.write(str(i)+'|')
        #ui = Gui(game)
        #gui.start()
        solved = mySearch.search()
        #f.write(str((datetime.now()-startTime).total_seconds()) + '|')
        space = len(mySearch.open) + len(mySearch.closed)
        print("runtime:",(datetime.now()-startTime).total_seconds(), "| size:", space)
        #f.write(str(space) + '\n')
        #gui = Gui(solved)
        #gui.start()
        #f.close()

###################################################


if __name__ =="__main__":
    main()
