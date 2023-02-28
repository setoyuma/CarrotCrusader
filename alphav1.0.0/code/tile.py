import pygame as pg
from settings import *
from support import *

class Tile(pg.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pg.Surface((TILE_SIZE,TILE_SIZE))
        # self.image = img
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)

class StaticTile(Tile):
	def __init__(self,pos,groups,surface):
		super().__init__(pos,groups)
		self.image = surface 

class AnimatedTile(Tile):
	def __init__(self,size,x,y,path):
		super().__init__(size,x,y)
		self.frames = import_folder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,shiftx,shifty):
		self.animate()
		self.rect.x += shiftx
		self.rect.y += shifty
    