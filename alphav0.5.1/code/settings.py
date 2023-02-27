import pygame as pg
GAMEICON = pg.image.load('../graphics/gameicon.ico')
vertical_tile_number = 16
tile_size = 32

screen_height = (vertical_tile_number*2) * tile_size
screen_width = 1200

# camera
CAMERA_BORDERS = {
	'left': 100,
	'right': 200,
	'top':100,
	'bottom': 150
}