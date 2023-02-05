import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self,pos,size,img):
        super().__init__()
        self.image = img
        # self.image = pg.image.load('../assets/tiles/Classic.png')
        # self.image = pg.image.load('../assets/tiles/ATOT/CTOS_Floor.png')
        # self.image = pg.Surface((size,size))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self,xShift):
        self.rect.x += xShift