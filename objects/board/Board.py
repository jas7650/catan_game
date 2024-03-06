# from .NumberTile import NumberTile
# from .Port import Port
# from .Tile import Tile
from .TileEnum import TileEnum
import numpy as np
import random

num_cols = [3, 4, 5, 4, 3]

class Board(object):
    def __init__(self):
        self.create_board()


    def create_board(self):
        tiles_dict = {}
        tiles = []
        for resource in TileEnum:
            tiles_dict[TileEnum(resource.value).name] = 0

        for value in num_cols:
            row = []
            for i in range(value):
                resource_value = (int)(random.random() * (TileEnum.DESERT.value + 1))
                while tiles_dict[TileEnum(resource_value).name] == TileEnum.getMaxResourceTiles(resource_value):
                    resource_value = (int)(random.random() * (TileEnum.DESERT.value + 1))
                tiles_dict[TileEnum(resource_value).name] += 1
                row.append(TileEnum(resource_value).value)
            tiles.append(row)
        self.tiles = tiles


    def get_board(self):
        return self.tiles
