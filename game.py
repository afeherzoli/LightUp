#from re import I
from tile import Tile as Tile
from get_level import getLevel
from itertools import product


class Game:

    # Describe the state change if a tile lights up
    _change_if_lit = {
        Tile.EMPTY: Tile.LIT,
        Tile.LIGHT: Tile.BADLIGHT,
        Tile.BADLIGHT: Tile.BADLIGHT,
        Tile.LIT: Tile.LIT,
        Tile.NOLIGHT: Tile.LITNOLIGHT,
        Tile.LITNOLIGHT: Tile.LITNOLIGHT}
    
    # Describe the state change if a tile is no longer lit
    _change_if_not_lit = {
        Tile.EMPTY: Tile.EMPTY,
        Tile.LIGHT: Tile.LIGHT,
        Tile.BADLIGHT: Tile.LIGHT,
        Tile.LIT: Tile.EMPTY,
        Tile.NOLIGHT: Tile.NOLIGHT,
        Tile.LITNOLIGHT: Tile.NOLIGHT}
    
    # Describe the state change if numbered tile is satisfiable
    _change_if_can_satisfy = {
        Tile.ZERO: Tile.ZERO,
        Tile.BADZERO: Tile.ZERO,
        Tile.ONE: Tile.ONE,
        Tile.BADONE: Tile.ONE,
        Tile.TWO: Tile.TWO,
        Tile.BADTWO: Tile.TWO,
        Tile.THREE: Tile.THREE,
        Tile.BADTHREE: Tile.THREE,
        Tile.FOUR: Tile.FOUR,
        Tile.BADFOUR: Tile.FOUR,
        Tile.BLOCK: Tile.BLOCK}
    
    # Describe the state change if numbered tile is no longer satisfiable
    _change_if_can_not_satisfy = {
        Tile.ZERO: Tile.BADZERO,
        Tile.BADZERO: Tile.BADZERO,
        Tile.ONE: Tile.BADONE,
        Tile.BADONE: Tile.BADONE,
        Tile.TWO: Tile.BADTWO,
        Tile.BADTWO: Tile.BADTWO,
        Tile.THREE: Tile.BADTHREE,
        Tile.BADTHREE: Tile.BADTHREE,
        Tile.FOUR: Tile.BADFOUR,
        Tile.BADFOUR: Tile.BADFOUR,
        Tile.BLOCK: Tile.BLOCK}

    def __init__(self, lvlId=1):
        self.board = getLevel(lvlId)
        self.size = len(self.board[0])

    def __hash__(self):
        return hash(str(self.board))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.board == other.board

    # Places or removes a lightsource in the given positon then updates the gameboard
    def place_light(self, row, column):
        row = int(row)
        column = int(column)

        match self.board[row][column]: 
            case Tile.EMPTY | Tile.LIT:
                self.board[row][column] = Tile.LIGHT
                self._refresh_grid(row, column)
            case Tile.LIGHT | Tile.BADLIGHT:
                self.board[row][column] = Tile.EMPTY
                self._refresh_grid(row, column)

    # Places a no lightsource indicator in the given position
    def place_no_light(self, row, column):
        row = int(row)
        column = int(column)

        match self.board[row][column]:
            case Tile.EMPTY:
                self.board[row][column] = Tile.NOLIGHT
            case Tile.LIT:
                self.board[row][column] = Tile.LITNOLIGHT
            case Tile.NOLIGHT:
                self.board[row][column] = Tile.EMPTY
            case Tile.LITNOLIGHT:
                self.board[row][column] = Tile.LIT

    # Returns whether a tile is lit or not
    def _is_tile_lit(self, row, column):
        base_row = row
        base_column = column

        row -= 1
        while(0 <= row < self.size):
            if self.board[row][column] in [Tile.LIGHT, Tile.BADLIGHT]:
                return True
            elif self._is_tile_solid(row, column):
                break
            row -= 1

        row = base_row
        row += 1
        while(0 <= row < self.size):
            if self.board[row][column] in [Tile.LIGHT, Tile.BADLIGHT]:
                return True
            elif self._is_tile_solid(row, column):
                break
            row += 1

        row = base_row
        column -= 1
        while(0 <= column < self.size):
            if self.board[row][column] in [Tile.LIGHT, Tile.BADLIGHT]:
                return True
            elif self._is_tile_solid(row, column):
                break
            column -= 1

        column = base_column
        column += 1
        while(0 <= column < self.size):
            if self.board[row][column] in [Tile.LIGHT, Tile.BADLIGHT]:
                return True
            elif self._is_tile_solid(row, column):
                break
            column += 1

        return False

    # Returns whether a tile stops light or not
    def _is_tile_solid(self, row, column):
        if self.board[row][column] in [
            Tile.ZERO, Tile.ONE, Tile.TWO, Tile.THREE, Tile.FOUR, Tile.BLOCK,
            Tile.BADZERO, Tile.BADONE, Tile.BADTWO, Tile.BADTHREE, Tile.BADFOUR
        ]:
            return True
        else:
            return False
    
    # Returns whether a numbered tile can still be satisfied
    def _can_satisfy(self, row, column):
        match self.board[row][column]:
            case Tile.ZERO | Tile.BADZERO:
                num_at_positon = 0
            case Tile.ONE | Tile.BADONE:
                num_at_positon = 1
            case Tile.TWO | Tile.BADTWO:
                num_at_positon = 2
            case Tile.THREE | Tile.BADTHREE:
                num_at_positon = 3
            case Tile.FOUR | Tile.BADFOUR:
                num_at_positon = 4
            case _:
                raise ValueError("Not a numbered tile")
                    
        if self.num_of_lights_around(row, column) == num_at_positon:
            return True
        elif self.num_of_lights_around(row, column) > num_at_positon:
            return False
        elif self.num_of_lights_around(row, column) + self.num_of_emptys_around(row, column) >= num_at_positon:
            return True

    # Returns the number of ligths around a given positon, used for checking restrictions
    def num_of_lights_around(self, row, column):
        lights = 0

        if row != 0 and self.board[row-1][column] in [Tile.LIGHT, Tile.BADLIGHT]:
            lights += 1

        if row != self.size-1 and self.board[row+1][column] in [Tile.LIGHT, Tile.BADLIGHT]:
            lights += 1

        if column != 0 and self.board[row][column-1] in [Tile.LIGHT, Tile.BADLIGHT]:
            lights += 1

        if column != self.size-1 and self.board[row][column+1] in [Tile.LIGHT, Tile.BADLIGHT]:
            lights += 1

        return lights

    # Returns the number of emptys around a given positon, used for heuristic and board legitness
    def num_of_emptys_around(self, row, column):
        return len(self.get_emptys_around(row, column))
        """
        empty_tiles = 0

        if row != 0 and self.board[row-1][column] == Tile.EMPTY:
            empty_tiles += 1

        if row != self.size-1 and self.board[row+1][column] == Tile.EMPTY:
            empty_tiles += 1

        if column != 0 and self.board[row][column-1] == Tile.EMPTY:
            empty_tiles += 1

        if column != self.size-1 and self.board[row][column+1] == Tile.EMPTY:
            empty_tiles += 1

        return empty_tiles
        """

    def get_emptys_around(self, row, column):
        emptys_around = []

        if row != 0 and self.board[row-1][column] == Tile.EMPTY:
            emptys_around.append((row-1, column))

        if row != self.size-1 and self.board[row+1][column] == Tile.EMPTY:
            emptys_around.append((row+1, column))

        if column != 0 and self.board[row][column-1] == Tile.EMPTY:
            emptys_around.append((row, column-1))

        if column != self.size-1 and self.board[row][column+1] == Tile.EMPTY:
            emptys_around.append((row, column+1))

        return emptys_around

    # Refreshes grid, used after changes to update the board
    # row and column arguments states the place of change
    def _refresh_grid(self, row, column):
        for i in range(self.size):
            if not self._is_tile_solid(i, column):
                if self._is_tile_lit(i, column):
                    self.board[i][column] = self._change_if_lit[self.board[i][column]]
                else:
                    self.board[i][column] = self._change_if_not_lit[self.board[i][column]]

            if not self._is_tile_solid(row, i):
                if self._is_tile_lit(row, i):
                    self.board[row][i] = self._change_if_lit[self.board[row][i]]
                else:
                    self.board[row][i] = self._change_if_not_lit[self.board[row][i]]

        match row:
            case 0:
                row_start = 0
                row_end = 2
            case self.size:
                row_start = self.size - 1
                row_end = self.size
            case _:
                row_start = row - 1
                row_end = row + 1

        match column:
            case 0:
                column_start = 0
                column_end = 2
            case self.size:
                column_start = self.size - 1
                column_end = self.size
            case _:
                column_start = row - 1
                column_end = row + 1

        for row, column in product(range(row_start, row_end), range(self.size)):
            if self._is_tile_solid(row, column) and self.board[row][column]!=Tile.BLOCK:
                if self._can_satisfy(row, column):
                    self.board[row][column] = self._change_if_can_satisfy[self.board[row][column]]
                else:
                    self.board[row][column] = self._change_if_can_not_satisfy[self.board[row][column]]

        for row, column in product(range(self.size), range(column_start, column_end)):
            if self._is_tile_solid(row, column) and self.board[row][column]!=Tile.BLOCK:
                if self._can_satisfy(row, column):
                    self.board[row][column] = self._change_if_can_satisfy[self.board[row][column]]
                else:
                    self.board[row][column] = self._change_if_can_not_satisfy[self.board[row][column]]

    # Returns whether the winning conditions are met
    def is_game_won(self):
        for rows, columns in product(range(self.size), range(self.size)):
            if self.board[rows][columns] in [
                Tile.EMPTY, Tile.NOLIGHT, Tile.BADLIGHT, Tile.BADZERO, Tile.BADONE, Tile.BADTWO, Tile.BADTHREE, Tile.BADFOUR
            ]:
                return False
        return True

    # Checks the current boardstate that it's still solvable
    def is_board_state_legit(self):
        for rows, columns in product(range(self.size), range(self.size)):
            if self.board[rows][columns] in [
                Tile.BADLIGHT, Tile.BADZERO, Tile.BADONE, Tile.BADTWO, Tile.BADTHREE, Tile.BADFOUR
            ]:
                return False
        return True


def main():
    game = Game()


###################################################


if __name__ == "__main__":
    main()
