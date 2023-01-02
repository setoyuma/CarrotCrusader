import pygame as pg
from settings import *
from tileClass import Tile
from playerClass import Player
from mapData import WORLD_MAP
from debug import debug

class Level:
    def __init__(self) -> None:
        # self.displaySurface = surf
        self.displaySurface = pg.display.get_surface()
        #sprite group setup
        self.drawnSprites = YSortCameraGroup()
        self.collideSprites = pg.sprite.Group()

        self.createMap()

    def createMap(self):
        for rowIndex,row in enumerate(WORLD_MAP):
            for colIndex,col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == "x":
                    Tile((x,y),[self.drawnSprites,self.collideSprites])
                if col == "p":
                    self.player = Player((x,y),[self.drawnSprites],self.collideSprites)


    def run(self):
        #update and draw the game
        self.drawnSprites.customDraw(self.player)
        self.drawnSprites.update()
        # self.player.update()  #uncomment for fps boost????
        debug(self.player.direction)




class YSortCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pg.display.get_surface()

        self.halfWidth = self.displaySurface.get_size()[0] // 2 #used to keep player center screen
        self.halfHeight = self.displaySurface.get_size()[1] // 2

        self.offset = pg.math.Vector2() #offset of drawn images

    def customDraw(self,player):
        #getting offset
        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image,offsetPos)