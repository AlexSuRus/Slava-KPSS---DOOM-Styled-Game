import pygame as pg
from settings import BASE_RES

kpss = pg.image.load('slava.jpg')

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, _, 1, 1, 1, 1, _, 1, _, 1],
    [1, _, 1, _, _, 1, _, _, _, 1],
    [1, _, 1, _, _, 1, _, 1, _, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'white', (pos[0] * BASE_RES, pos[1] * BASE_RES, BASE_RES, BASE_RES), 2)
         for pos in self.world_map
         ]
