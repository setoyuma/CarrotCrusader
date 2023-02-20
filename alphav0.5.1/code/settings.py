import pygame as pg

GAMEICON = pg.image.load('../graphics/gameicon.ico')

vertical_tile_number = 22
tile_size = 32

screen_height = vertical_tile_number * tile_size
screen_width = 1200

DISPLAY = pg.Surface((440,362)) # used as the surface for rendering, which is scaled 2.75x
