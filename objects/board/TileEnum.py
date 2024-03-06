from enum import Enum
import pygame

WOOD_TILES = 4
BRICK_TILES = 3
SHEEP_TILES = 4
ORE_TILES = 3
WHEAT_TILES = 4
DESERT_TILES = 1

class TileEnum(Enum):
    WOOD = 0
    BRICK = 1
    SHEEP = 2
    ORE = 3
    WHEAT = 4
    DESERT = 5


    def getMaxResourceTiles(resource_value):
        if resource_value == TileEnum.WOOD.value:
            return WOOD_TILES
        elif resource_value == TileEnum.BRICK.value:
            return BRICK_TILES
        elif resource_value == TileEnum.SHEEP.value:
            return SHEEP_TILES
        elif resource_value == TileEnum.ORE.value:
            return ORE_TILES
        elif resource_value == TileEnum.WHEAT.value:
            return WHEAT_TILES
        else:
            return DESERT_TILES


    def getResourceColor(resource_value):
        if resource_value == TileEnum.WOOD.value:
            return pygame.Color('forestgreen')
        elif resource_value == TileEnum.BRICK.value:
            return pygame.Color('coral3')
        elif resource_value == TileEnum.SHEEP.value:
            return pygame.Color('darkolivegreen1')
        elif resource_value == TileEnum.ORE.value:
            return pygame.Color('thistle3')
        elif resource_value == TileEnum.WHEAT.value:
            return pygame.Color('gold')
        else:
            return pygame.Color('lightgoldenrod3')


def getResourceName(resource_value):
    if resource_value == TileEnum.WOOD.value:
        return "Wood"
    elif resource_value == TileEnum.BRICK.value:
        return "Brick"
    elif resource_value == TileEnum.SHEEP.value:
        return "Sheep"
    elif resource_value == TileEnum.ORE.value:
        return "Ore"
    elif resource_value == TileEnum.WHEAT.value:
        return "Wheat"
    else:
        return "Desert"
