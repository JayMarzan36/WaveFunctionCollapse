class Tile:
    def __init__(self, image, edges):
        self.image = image
        self.edges = edges
        self.index = None
        self.rules = [set() for _ in range(4)]

    def set_Rules(self, options):
        for i in range(4):
            for option in options:
                if self.edges[i] == option.edges[(i + 2) % 4]:
                    self.rules[i].add(option.index)


    def custom_deepcopy(self):
        new_tile = Tile(self.image, self.edges[:])
        new_tile.index = self.index
        new_tile.rules = [rule.copy() for rule in self.rules]
        return new_tile
