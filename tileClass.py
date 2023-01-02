import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self,pos,groups) -> None:
        super().__init__(groups)
        self.image = pg.image.load('./imgs/tiles/Classic.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10) #-10 shrinks by 5px