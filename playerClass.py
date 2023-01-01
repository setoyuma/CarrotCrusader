import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,groups) -> None:
        super().__init__(groups)
        self.image = pg.image.load('./imgs/player/vegnath.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)