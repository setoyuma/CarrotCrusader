from settings import vertical_tile_number, tile_size, screen_width
import pygame as pg
from tiles import AnimatedTile, StaticTile
from support import import_folder
from random import choice, randint

class Sky:
	def __init__(self,horizon):
		self.top = pg.image.load('../graphics/decoration/sky/sky_top.png').convert()
		self.bottom = pg.image.load('../graphics/decoration/sky/sky_bottom.png').convert()
		self.middle = pg.image.load('../graphics/decoration/sky/DarkSky.png').convert()
		self.horizon = horizon

		# # stretch 
		self.top = pg.transform.scale(self.top,(screen_width,tile_size))
		self.bottom = pg.transform.scale(self.bottom,(screen_width,tile_size))
		self.middle = pg.transform.scale(self.middle,(screen_width,tile_size))

	def draw(self,surface):
		for row in range(vertical_tile_number):
			y = row * tile_size
			if row < self.horizon:
				surface.blit(self.top,(0,y))
			elif row == self.horizon:
				surface.blit(self.middle,(0,y))
			else:
				surface.blit(self.bottom,(0,y))
