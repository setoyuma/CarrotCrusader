import pygame as pg, os, csv
from settings02 import *
from playerClass import Player
from tileClass import Tile

class Level():
    def __init__(self,mapData,surface) -> None:
        self.displaySurface = surface
        self.DrawMap(mapData)
        self.worldShift = 0
        self.currentPlayerX = 0
        
    def DrawMap(self,mapData):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        for rowIndex, row in enumerate(mapData):
            for colIndex, cell in enumerate(row):
                x = colIndex*TILESIZE
                y = rowIndex*TILESIZE

                match cell:
                    case'0':
                        tile = Tile((x,y),GAMETILES["BreakableBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["BreakableBlock"])
                        # self.tiles.add(tile)
                    case'1':
                        tile = Tile((x,y),GAMETILES["GrassBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["GrassBlock"])
                        # self.tiles.add(tile)
                    case'2':
                        tile = Tile((x,y),GAMETILES["CastleHallBrickFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["CastleHallBrickFloor"])
                        # self.tiles.add(tile)
                    case'3':
                        tile = Tile((x,y),GAMETILES["CastleHallFloorPillar"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["CastleHallFloorPillar"])
                        # self.tiles.add(tile)
                    case'4':
                        tile = Tile((x,y),GAMETILES["BrickBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["BrickBlock"])
                        # self.tiles.add(tile)
                    case'5':
                        tile = Tile((x,y),GAMETILES["CastleHallFloorSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["CastleHallFloorSupport"])
                        # self.tiles.add(tile)
                    case'6':
                        tile = Tile((x,y),GAMETILES["ChapelFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["ChapelFloor"])
                        # self.tiles.add(tile)
                    case'7':
                        tile = Tile((x,y),GAMETILES["ChapelSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["ChapelSupport"])
                        # self.tiles.add(tile)
                    case'8':
                        tile = Tile((x,y),GAMETILES["IceFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["IceFloor"])
                        # self.tiles.add(tile)
                    case'9':
                        tile = Tile((x,y),GAMETILES["IceyBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["IceyBlock"])
                        # self.tiles.add(tile)
                    case'10':
                        tile = Tile((x,y),GAMETILES["DrakeGround"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["DrakeGround"])
                        # self.tiles.add(tile)
                    case'11':
                        tile = Tile((x,y),GAMETILES["MagmaPoolBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["MagmaPoolBlock"])
                        # self.tiles.add(tile)
                    case'12':
                        tile = Tile((x,y),GAMETILES["WonderBlockFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["WonderBlockFloor"])
                        # self.tiles.add(tile)
                    case'13':
                        tile = Tile((x,y),GAMETILES["WonderBlockSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["WonderBlockSupport"])
                        # self.tiles.add(tile)
                    case'14':
                        tile = Tile((x,y),GAMETILES["PillarBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["PillarBlock"])
                        # self.tiles.add(tile)
                    case'15':
                        tile = Tile((x,y),GAMETILES["PillarSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["PillarSupport"])
                        # self.tiles.add(tile)
                    case'16':
                        tile = Tile((x,y),GAMETILES["GhostTrainFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["GhostTrainFloor"])
                        # self.tiles.add(tile)
                    case'17':
                        tile = Tile((x,y),GAMETILES["HauntedPrisonFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["HauntedPrisonFloor"])
                        # self.tiles.add(tile)
                    case'18':
                        tile = Tile((x,y),GAMETILES["HauntedPrisonSupport"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["HauntedPrisonSupport"])
                        # self.tiles.add(tile)
                    case'19':
                        tile = Tile((x,y),GAMETILES["MasterChamberFloor"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["MasterChamberFloor"])
                        # self.tiles.add(tile)
                    case'20':
                        tile = Tile((x,y),GAMETILES["MasterChamberSigil"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["MasterChamberSigil"])
                        # self.tiles.add(tile)
                    case'21':
                        tile = Tile((x,y),GAMETILES["MasterChamberPillarTop"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["MasterChamberPillarTop"])
                        # self.tiles.add(tile)
                    case'22':
                        tile = Tile((x,y),GAMETILES["MasterChamberPillar"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["MasterChamberPillar"])
                        # self.tiles.add(tile)
                    case'23':
                        tile = Tile((x,y),GAMETILES["ClassicBlock"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["ClassicBlock"])
                        # self.tiles.add(tile)
                    case '24':
                        self.playerSprite = Player((x,y),self.displaySurface)
                        # self.playerSprite.rect.inflate_ip(-15,0)
                        self.player.add(self.playerSprite)
                    case'25':
                        tile = Tile((x,y),GAMETILES["LevelEnd"])
                        self.tiles.add(tile)
                        # tile = Tile((x,y),GAMETILES["LevelEnd"])
                        # self.tiles.add(tile)
                        pass

    def cameraScroll(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x
        if playerX <= (WINDOWSIZE[0]/2)/6 and directionX < 0:
            self.worldShift = 2
            player.speed = 0
        elif playerX >= (WINDOWSIZE[0]/4) - (WINDOWSIZE[0]/8.5) and directionX > 0:
            self.worldShift = -2
            player.speed = 0
        else:
            self.worldShift = 0
            player.speed = 2

    def horizontalCollision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.onLeftWall = True
                    self.currentPlayerX = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.onRightWall = True
                    self.currentPlayerX = player.rect.right
            
        if player.onLeftWall and (player.rect.left < self.currentPlayerX or player.direction.x >= 0):
            player.onLeftWall = False
        if player.onRightWall and (player.rect.right < self.currentPlayerX or player.direction.x <= 0):
            player.onRightWall = False




    def verticalCollision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.airBorne = False
                    player.direction.y = 0
                    player.onGround = True
                
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.onCeiling = True

        if player.onGround and player.direction.y < 0 or player.direction.y > 1:
            player.onGround = False
        if player.onCeiling and player.direction.y > 0:
            player.onCeiling = False

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