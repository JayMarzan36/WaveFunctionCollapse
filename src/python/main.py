import sys, pygame

from Grid import Grid
from Tile import Tile

pygame.init()

width = 600
height = 600
rez = 5

display = pygame.display.set_mode((width, height), pygame.RESIZABLE)


def load_Image(path, rez, padding=0):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (rez - padding, rez - padding))
    return image


def main():
    options = []
    # [top, right, bottom, left]
    tile_Types = [
        {"name": "0", "edges": [1, 0, 1, 0]},
        {"name": "1", "edges": [0, 1, 0, 1]},
        {"name": "2", "edges": [0, 1, 1, 0]},
        {"name": "3", "edges": [0, 0, 1, 1]},
        {"name": "4", "edges": [1, 0, 0, 1]},
        {"name": "5", "edges": [1, 1, 0, 0]},
        {"name": "6", "edges": [0, 1, 1, 0]},
        {"name": "7", "edges": [0, 0, 0, 1]},
        {"name": "8", "edges": [1, 1, 1, 1]}


    ]
    for i, tile_type in enumerate(tile_Types):
        image = load_Image(f"./tile_Images/{tile_type['name']}.png", rez)
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
