import sys, pygame

from Grid import Grid
from Tile import Tile

pygame.init()

width = 400
height = 400
rez = 4

display = pygame.display.set_mode((width, height), pygame.RESIZABLE)


def load_Image(path, rez, padding = 0):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (rez - padding, rez - padding))
    return image


def main():
    options = []
    # [top, right, bottom, left]
    tile_Types = [
        {"name": "water", "edges": [0, 1, 1, 0]},
        {"name": "grass", "edges": [1, 1, 1, 1]},
        {"name": "tree", "edges": [1, 1, 1, 1]},
        {"name": "sand", "edges": [2, 2, 2, 2]}
    ]
    for i, tile_type in enumerate(tile_Types):
        image = load_Image(f"./tile_Images/smaller_Images/{tile_type['name']}.png", rez)
        # image = load_Image(f"./tile_Images/{tile_type['name']}.png", rez)
        options.append(Tile(image, tile_type["edges"]))



    for i, tile in enumerate(options):
        tile.index = i
        tile.set_Rules(options)

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
