import random
from Cell import Cell


class Grid:
    def __init__(self, width, height, rez, options):
        self.width = width
        self.height = height
        self.rez = rez
        self.cell_W = self.width // self.rez
        self.cell_H = self.height // self.rez
        self.grid = []
        self.options = options

    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)

    def initiate(self):
        self.grid = []
        for i in range(self.cell_W):
            row = []
            for j in range(self.cell_H):
                cell = Cell(i, j, self.rez, [option.custom_deepcopy() for option in self.options])
                row.append(cell)
            self.grid.append(row)
        print(f"Grid initialized with {self.cell_W} columns and {self.cell_H} rows.")
        for row in self.grid:
            for cell in row:
                print(f"Cell ({cell.x}, {cell.y}) options: {[tile.index for tile in cell.options]}")

    def heuristic_Pick(self):

        # shallow copy of a grid
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key=lambda x: x.entropy())

        filtered_grid = list(filter(lambda x: x.entropy() > 1, grid_copy))
        if not filtered_grid:
            return None

        least_entropy_cell = filtered_grid[0]
        filtered_grid = list(filter(lambda x: x.entropy() == least_entropy_cell.entropy(), filtered_grid))

        pick = random.choice(filtered_grid)
        return pick

    def propagate(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if not self.grid[i][j].collapsed:
                    cumulative_Valid_Options = set(range(len(self.options)))

                    # Check cell above
                    if i > 0:
                        cell_Above = self.grid[i - 1][j]
                        valid_Options = set()
                        for option in cell_Above.options:
                            valid_Options.update(option.rules[2])
                        cumulative_Valid_Options.intersection_update(valid_Options)

                    # Check cell right
                    if j < self.cell_H - 1:
                        cell_Right = self.grid[i][j + 1]
                        valid_Options = set()
                        for option in cell_Right.options:
                            valid_Options.update(option.rules[3])
                        cumulative_Valid_Options.intersection_update(valid_Options)

                    # Check cell below
                    if i < self.cell_W - 1:
                        cell_Down = self.grid[i + 1][j]
                        valid_Options = set()
                        for option in cell_Down.options:
                            valid_Options.update(option.rules[0])
                        cumulative_Valid_Options.intersection_update(valid_Options)

                    # Check cell left
                    if j > 0:
                        cell_Left = self.grid[i][j - 1]
                        valid_Options = set()
                        for option in cell_Left.options:
                            valid_Options.update(option.rules[1])
                        cumulative_Valid_Options.intersection_update(valid_Options)

                    # if any(option.index in [2, 3] for option in self.grid[i][j].options):
                    #     cumulative_Valid_Options.intersection_update(
                    #         [option.index for option in self.options if option.index in [0, 1]])

                    self.grid[i][j].options = [self.options[idx] for idx in cumulative_Valid_Options]
                    self.grid[i][j].update()

    def collapse(self):
        pick = self.heuristic_Pick()
        if pick:
            print(f"Collapsing cell at ({pick.x}, {pick.y}) with options: {[tile.index for tile in pick.options]}")
            self.grid[pick.x][pick.y].observe()
            self.propagate()
        else:
            return
