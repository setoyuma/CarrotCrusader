import pygame as pg
from support import importFolder


class Tile(pg.sprite.Sprite):
    def __init__(self,size,x,y,path):
        super().__init__()
        # self.image = img
        # self.image = importFolder(path)
        self.image = pg.Surface((size,size))
        self.rect = self.image.get_rect(topleft = (x,y))
        
        # self.image = pg.image.load('../assets/tiles/Classic.png')
        # self.image = pg.image.load('../assets/tiles/ATOT/CTOS_Floor.png')
        # self.image = pg.Surface((size,size))
        # self.image.fill('red')
        # self.rect = self.image.get_rect(topleft=(x,y))

    def update(self,xShift):
        self.rect.x += xShift

class StaticTile(Tile):
	def __init__(self,size,x,y,surface,path):
		super().__init__(size,x,y,path)
		self.image = surface 

class AnimatedTile(Tile):
	def __init__(self,size,x,y,path):
		super().__init__(size,x,y,path)
		self.frames = importFolder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
        

	def animate(self):
		self.frame_index += self.animSpeed
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,shift):
		self.animate()
		self.rect.x += shift

class AnimBlock(AnimatedTile):
    def __init__(self,size,x,y,path):
        self.animSpeed = 0.15
        super().__init__(size,x,y,path)
        center_x = x + int(size/2)
        center_y = y + int(size/2)
        self.rect = self.image.get_rect(center=(center_x,center_y))
