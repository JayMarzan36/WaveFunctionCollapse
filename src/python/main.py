import sys, pygame

from Grid import Grid
from Tile import Tile

pygame.init()

width = 600
height = 600
rez = 3

display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Wave Function Collapse")


def load_image(path, rez, padding=0):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (rez - padding, rez - padding))
    return image


def main():
    options = []
    # [top, right, bottom, left], maybe
    tile_Types = [
        {"name": "9", "edges": [0, 1, 0, 1]},
        {"name": "10", "edges": [1, 2, 1, 2]},
        {"name": "11", "edges": [2, 0, 2, 0]}
    ]
    for i, tile_type in enumerate(tile_Types):
        image = load_image(f"./tile_Images/{tile_type['name']}.png", rez)
        options.append(Tile(image, tile_type["edges"]))

    for i, tile in enumerate(options):
        tile.index = i
        tile.set_rules(options)

    wave = Grid(width, height, rez, options)
    wave.initiate()

    run = True

    while run:
        display.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    wave = Grid(width, height, rez, options)
                    wave.initiate()

        wave.draw(display)

        wave.collapse()

        pygame.display.flip()


if __name__ == "__main__":
    main()