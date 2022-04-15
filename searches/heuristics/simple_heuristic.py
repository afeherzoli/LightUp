from tile import Tile as Tile
from game import Game

_tile_to_int = {
        Tile.ZERO : 0,
        Tile.ONE : 1,
        Tile.TWO  : 2,
        Tile.THREE : 3,
        Tile.FOUR : 4,
        Tile.BADZERO : 0,
        Tile.BADONE : 1,
        Tile.BADTWO  : 2,
        Tile.BADTHREE : 3,
        Tile.BADFOUR : 4,
    }

# This heuristic function counts the sum of numbers on the numbered tiles
# then subtracts the number of lamps around each numbered tile
def simple_heuristic(game):
        numbers = 0
        satisfaction = 0
        for rows in range(game.size):
            for columns in range(game.size):
                if game.board[rows][columns] in [Tile.ZERO, Tile.ONE, Tile.TWO, Tile.THREE, Tile.FOUR]:
                    numbers += _tile_to_int[game.board[rows][columns]]
                    satisfaction += game.num_of_lights_around(rows, columns)
        return numbers - satisfaction
