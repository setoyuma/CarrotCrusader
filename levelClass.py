import pygame as pg
from settings import *
from tileClass import Tile
from playerClass import Player
from mapData import WORLD_MAP

class Level:
    def __init__(self,surf) -> None:
        self.displaySurface = surf
        # self.displaySurface = pg.display.get_surface()
        #sprite group setup
        self.drawnSprites = pg.sprite.Group()
        self.collideSprites = pg.sprite.Group()

        self.createMap()

    def createMap(self):
        for rowIndex,row in enumerate(WORLD_MAP):
            for colIndex,col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == "x":
                    Tile((x,y),[self.drawnSprites])


    def run(self):
        #update and draw the game
        self.drawnSprites.draw(self.displaySurface)