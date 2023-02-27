import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pg.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)