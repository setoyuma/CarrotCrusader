import pygame as pg, os, csv
from settings02 import *
from playerClass import Player
from tileClass import Tile

class Level():
    def __init__(self,mapData,surface) -> None:
        self.displaySurface = surface
        self.DrawMap(mapData)
        self.worldShift = 0


    def DrawMap(self,mapData):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        for rowIndex, row in enumerate(mapData):
            for colIndex, cell in enumerate(row):
                x = colIndex*TILESIZE
                y = rowIndex*TILESIZE

                match cell:
                    case'0':
                        tile = Tile((x,y),TILESIZE,GAMETILES["BreakableBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["BreakableBlock"])
                        # self.tiles.add(tile)
                    case'1':
                        tile = Tile((x,y),TILESIZE,GAMETILES["GrassBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["GrassBlock"])
                        # self.tiles.add(tile)
                    case'2':
                        tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallBrickFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallBrickFloor"])
                        # self.tiles.add(tile)
                    case'3':
                        tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallFloorPillar"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallFloorPillar"])
                        # self.tiles.add(tile)
                    case'4':
                        tile = Tile((x,y),TILESIZE,GAMETILES["BrickBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["BrickBlock"])
                        # self.tiles.add(tile)
                    case'5':
                        tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallFloorSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallFloorSupport"])
                        # self.tiles.add(tile)
                    case'6':
                        tile = Tile((x,y),TILESIZE,GAMETILES["ChapelFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["ChapelFloor"])
                        # self.tiles.add(tile)
                    case'7':
                        tile = Tile((x,y),TILESIZE,GAMETILES["ChapelSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["ChapelSupport"])
                        # self.tiles.add(tile)
                    case'8':
                        tile = Tile((x,y),TILESIZE,GAMETILES["IceFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["IceFloor"])
                        # self.tiles.add(tile)
                    case'9':
                        tile = Tile((x,y),TILESIZE,GAMETILES["IceyBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["IceyBlock"])
                        # self.tiles.add(tile)
                    case'10':
                        tile = Tile((x,y),TILESIZE,GAMETILES["DrakeGround"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["DrakeGround"])
                        # self.tiles.add(tile)
                    case'11':
                        tile = Tile((x,y),TILESIZE,GAMETILES["MagmaPoolBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["MagmaPoolBlock"])
                        # self.tiles.add(tile)
                    case'12':
                        tile = Tile((x,y),TILESIZE,GAMETILES["WonderBlockFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["WonderBlockFloor"])
                        # self.tiles.add(tile)
                    case'13':
                        tile = Tile((x,y),TILESIZE,GAMETILES["WonderBlockSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["WonderBlockSupport"])
                        # self.tiles.add(tile)
                    case'14':
                        tile = Tile((x,y),TILESIZE,GAMETILES["PillarBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["PillarBlock"])
                        # self.tiles.add(tile)
                    case'15':
                        tile = Tile((x,y),TILESIZE,GAMETILES["PillarSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["PillarSupport"])
                        # self.tiles.add(tile)
                    case'16':
                        tile = Tile((x,y),TILESIZE,GAMETILES["GhostTrainFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["GhostTrainFloor"])
                        # self.tiles.add(tile)
                    case'17':
                        tile = Tile((x,y),TILESIZE,GAMETILES["HauntedPrisonFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["HauntedPrisonFloor"])
                        # self.tiles.add(tile)
                    case'18':
                        tile = Tile((x,y),TILESIZE,GAMETILES["HauntedPrisonSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["HauntedPrisonSupport"])
                        # self.tiles.add(tile)
                    case'19':
                        tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberFloor"])
                        # self.tiles.add(tile)
                    case'20':
                        tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberSigil"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberSigil"])
                        # self.tiles.add(tile)
                    case'21':
                        tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberPillarTop"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberPillarTop"])
                        # self.tiles.add(tile)
                    case'22':
                        tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberPillar"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberPillar"])
                        # self.tiles.add(tile)
                    case'23':
                        tile = Tile((x,y),TILESIZE,GAMETILES["ClassicBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["ClassicBlock"])
                        # self.tiles.add(tile)
                    case '24':
                        self.playerSprite = Player((x,y),self.displaySurface)
                        # self.playerSprite.rect.inflate_ip(-15,0)
                        self.player.add(self.playerSprite)
                    case'25':
                        tile = Tile((x,y),TILESIZE,GAMETILES["LevelEnd"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),TILESIZE,GAMETILES["LevelEnd"])
                        # self.tiles.add(tile)
                        pass






    def cameraScroll(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x
        if playerX <= (WINDOWSIZE[0]/2)/6 and directionX < 0:
            self.worldShift = 3
            player.speed = 0
        elif playerX >= (WINDOWSIZE[0]/4) - (WINDOWSIZE[0]/8.5) and directionX > 0:
            self.worldShift = -3
            player.speed = 0
        else:
            self.worldShift = 0
            player.speed = 3

    def horizontalCollision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    
    def verticalCollision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.airBorne = False
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def Run(self):
        
        #Map Tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.cameraScroll()
        
        #player
        self.player.update()
        self.horizontalCollision()
        self.verticalCollision()
        self.player.draw(self.displaySurface)