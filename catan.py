import pygame
import numpy as np
from math import *
from objects.board.Board import Board
from objects.board.TileEnum import TileEnum


TILE_RADIUS = 75
HORIZONTAL_OFFSET = sqrt(3) * TILE_RADIUS
VERTICAL_OFFSET = 3/2 * TILE_RADIUS
ROW_OFFSETS = [HORIZONTAL_OFFSET, HORIZONTAL_OFFSET/2, 0, HORIZONTAL_OFFSET/2, HORIZONTAL_OFFSET]


def main():
    global screen
    global board
    pygame.init()
    info = pygame.display.Info()
    screen_width = info.current_w-TILE_RADIUS
    screen_height = info.current_h-TILE_RADIUS
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    board = Board()
    draw_board(board.get_board(), screen_width, screen_height)
    pygame.display.update()

    mainLoop = True

    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
        pygame.display.update()

    pygame.quit()


def draw_board(tiles, screen_width, screen_height):
    row_num = 0
    for row in tiles:
        row_offset = ROW_OFFSETS[row_num]
        col_num = 0
        for col in row:
            draw_regular_polygon(screen, TileEnum.getResourceColor(col), 6, TILE_RADIUS, (floor(HORIZONTAL_OFFSET*(col_num+1)+row_offset+(screen_width/2-HORIZONTAL_OFFSET*2)), floor(VERTICAL_OFFSET*(row_num+1)+(screen_height/2-VERTICAL_OFFSET*3))))
            draw_regular_polygon(screen, pygame.Color('black'), 6, TILE_RADIUS, (floor(HORIZONTAL_OFFSET*(col_num+1)+row_offset+(screen_width/2-HORIZONTAL_OFFSET*2)), floor(VERTICAL_OFFSET*(row_num+1)+(screen_height/2-VERTICAL_OFFSET*3))), 2)
            col_num += 1
        row_num += 1


def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos((2 * pi * i / n) + pi/6), y + r * sin((2 * pi * i / n) + pi/6))
        for i in range(n)
    ], width)


if __name__ == "__main__":
    main()
