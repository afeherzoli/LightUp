from tile import Tile as Tile
from itertools import product
from game import Game

_tile_to_int = {
        Tile.ZERO : 0,
        Tile.ONE : 1,
        Tile.TWO  : 2,
        Tile.THREE : 3,
        Tile.FOUR : 4,
    }

# Before a search is started we solve a part of the game in advance
def preprocess(game: Game):
    # We can put lightsources and no-light indicators in places, where it's certian

    position_of_numbers = []

    for row, column in product(range(game.size), range(game.size)):
        match game.board[row][column]:
            case Tile.ZERO:
                for r, c in game.get_emptys_around(row, column):
                    game.place_no_light(r, c)

            case Tile.ONE:
                position_of_numbers.append((row, column))
                if game.num_of_lights_around(row, column) < 1:
                    if game.num_of_emptys_around(row, column) == 1: 
                        r, c = game.get_emptys_around(row, column)[0]
                        game.place_light(r, c)

            case Tile.TWO:
                position_of_numbers.append((row, column))
                if game.num_of_lights_around(row, column) < 2:
                    if game.num_of_emptys_around(row, column) == 2 - game.num_of_lights_around(row, column):
                        for r, c in game.get_emptys_around(row, column):
                            game.place_light(r, c)

            case Tile.THREE:
                position_of_numbers.append((row, column))
                if game.num_of_lights_around(row, column) < 3:
                    if game.num_of_emptys_around(row, column) == 3 - game.num_of_lights_around(row, column):
                        for r, c in game.get_emptys_around(row, column):
                            game.place_light(r, c)

            case Tile.FOUR:
                for r, c in game.get_emptys_around(row, column):
                    game.place_light(r, c)
    
    done = False

    while not done:
        done = True
        for row, column in position_of_numbers:
            match game.board[row][column]:
                case Tile.ONE:
                    if game.num_of_lights_around(row, column) < 1:
                        if game.num_of_emptys_around(row, column) == 1: 
                            r, c = game.get_emptys_around(row, column)[0]
                            game.place_light(r, c)
                            done = False

                case Tile.TWO:
                    if game.num_of_lights_around(row, column) < 2:
                        if game.num_of_emptys_around(row, column) == 2 - game.num_of_lights_around(row, column):
                            for r, c in game.get_emptys_around(row, column):
                                game.place_light(r, c)
                            done = False

                case Tile.THREE:
                    if game.num_of_lights_around(row, column) < 3:
                        if game.num_of_emptys_around(row, column) == 3 - game.num_of_lights_around(row, column):
                            for r, c in game.get_emptys_around(row, column):
                                game.place_light(r, c)
                            done = False



