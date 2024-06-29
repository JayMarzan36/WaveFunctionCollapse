import random
class Cell:
    def __init__(self, x, y, rez, options):
        self.x = x
        self.y = y
        self.rez = rez
        self.collapsed = False
        self.options = options[:]
        self.current = None

    def entropy(self):
        return len(self.options)

    def observe(self):
        self.collapsed = True
        self.current = random.choice(self.options)
        self.options = [self.current]

    def draw(self, win):
        if self.collapsed and self.current:
            win.blit(self.current.image, (self.x * self.rez, self.y * self.rez))

    def update(self):
        if not self.collapsed and len(self.options) == 1:
            self.observe()

    def custom_deepcopy(self):
        new_cell = Cell(self.x, self.y, self.rez, [option.custom_deepcopy() for option in self.options])
        new_cell.collapsed = self.collapsed
        new_cell.current = self.current.custom_deepcopy() if self.current else None
        return new_cell
