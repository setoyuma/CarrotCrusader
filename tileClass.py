import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self,pos,groups) -> None:
        super().__init__(groups)
        self.image = pg.image.load('./imgs/tiles/GrassBlock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)