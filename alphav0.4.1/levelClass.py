import pygame as pg, os, csv
from settings02 import *
from playerClass import Player
from tileClass import Tile,AnimBlock,StaticTile
from particles import ParticleEffect
# from SkyBox import SkyBox

class Level():
    def __init__(self,mapData,surface) -> None:
        self.displaySurface = surface
        self.DrawMap(mapData)
        self.worldShift = 0
        self.currentPlayerX = 0
        self.playerToScreenOffset = 4
        #dust
        self.dustSprite = pg.sprite.GroupSingle()

        #checks
        self.playerGrounded = False

        #decoration
        # self.sky = SkyBox(8)

    def createJumpParticle(self,pos):
        if self.player.sprite.facingRight:
            pos -= pg.math.Vector2(10,5)
        else:
            pos += pg.math.Vector2(10,-5)

        jumpParticleSprite = ParticleEffect(pos,'Jump')
        self.dustSprite.add(jumpParticleSprite)

    def groundedCheck(self):
        if self.player.sprite.onGround:
            self.playerGrounded = True
        else:
            self.playerGrounded = False

    def createLandingParticle(self):
        if not self.playerGrounded and self.player.sprite.onGround and not self.dustSprite.sprites():
            if self.player.sprite.facingRight:
                offset = pg.math.Vector2(5,15)
            else:
                offset = pg.math.Vector2(5,15)
            fallParticle = ParticleEffect(self.player.sprite.rect.midbottom - offset,"Land")
            self.dustSprite.add(fallParticle)

    def DrawMap(self,mapData):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        self.BG = pg.image.load('../assets/Sky/DarkSky.png')
        self.BG = pg.transform.scale(self.BG, (WINDOWSIZEHALF))
        for rowIndex, row in enumerate(mapData):
            for colIndex, cell in enumerate(row):
                x = colIndex*TILESIZE
                y = rowIndex*TILESIZE

                match cell:
                    case'0':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["BreakableBlock"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["BreakableBlock"],'')
                        # self.tiles.add(tile)
                    case'1':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["GrassBlock"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["GrassBlock"],'')
                        # self.tiles.add(tile)
                    case'2':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["CastleHallBrickFloor"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["CastleHallBrickFloor"],'')
                        # self.tiles.add(tile)
                    case'3':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["CastleHallFloorPillar"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["CastleHallFloorPillar"],'')
                        # self.tiles.add(tile)
                    case'4':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["BrickBlock"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["BrickBlock"],'')
                        # self.tiles.add(tile)
                    case'5':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["CastleHallFloorSupport"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["CastleHallFloorSupport"],'')
                        # self.tiles.add(tile)
                    case'6':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelFloor"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelFloor"],'')
                        # self.tiles.add(tile)
                    case'7':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelSupport"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelSupport"],'')
                        # self.tiles.add(tile)
                    case'8':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["IceFloor"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["IceFloor"],'')
                        # self.tiles.add(tile)
                    case'9':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["IceyBlock"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["IceyBlock"],'')
                        # self.tiles.add(tile)
                    case'10':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["DrakeGround"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["DrakeGround"],'')
                        # self.tiles.add(tile)
                    case'11':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES['MagmaPoolBlock'])
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["MagmaPoolBlock"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["MagmaPoolBlock"],'')
                        # self.tiles.add(tile)
                    case'12':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["WonderBlockFloor"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["WonderBlockFloor"],'')
                        # self.tiles.add(tile)
                    case'13':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["WonderBlockSupport"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["WonderBlockSupport"],'')
                        # self.tiles.add(tile)
                    case'14':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["PillarBlock"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["PillarBlock"],'')
                        # self.tiles.add(tile)
                    case'15':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["PillarSupport"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["PillarSupport"],'')
                        # self.tiles.add(tile)
                    case'16':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["GhostTrainFloor"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["GhostTrainFloor"],'')
                        # self.tiles.add(tile)
                    case'17':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["HauntedPrisonFloor"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["HauntedPrisonFloor"],'')
                        # self.tiles.add(tile)
                    case'18':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["HauntedPrisonSupport"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["HauntedPrisonSupport"],'')
                        # self.tiles.add(tile)
                    case'19':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["MasterChamberFloor"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["MasterChamberFloor"],'')
                        # self.tiles.add(tile)
                    case'20':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["MasterChamberSigil"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["MasterChamberSigil"],'')
                        # self.tiles.add(tile)
                    case'21':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["MasterChamberPillarTop"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["MasterChamberPillarTop"],'')
                        # self.tiles.add(tile)
                    case'22':
                        tile = AnimBlock(TILESIZE,x,y,GAMETILES["MasterChamberPillar"])
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["MasterChamberPillar"],'')
                        # self.tiles.add(tile)
                    case'23':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ClassicBlock"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["ClassicBlock"],'')
                        # self.tiles.add(tile)
                    case '24':
                        self.playerSprite = Player((x,y),self.displaySurface,self.createJumpParticle)
                        # self.playerSprite.rect.inflate_ip(-15,0)
                        self.player.add(self.playerSprite)
                    case'25':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["LevelEnd"],'')
                        self.tiles.add(tile)
                        # tile = StaticTile(TILESIZE,x,y,GAMETILES["LevelEnd"],'')
                        # self.tiles.add(tile)
                        pass
                    case'26':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["WoodFloor"],'')
                        self.tiles.add(tile)
                    case'27':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["TempleOfSixFloor"],'')
                        self.tiles.add(tile)
                    case'28':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["TempleOfSixFloorSupport"],'')
                        self.tiles.add(tile)
                    case'29':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["TempleOfSixFloorCracked"],'')
                        self.tiles.add(tile)
                    case'30':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["TempleOfSixFloorRug"],'')
                        self.tiles.add(tile)
                    case'31':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelFoundation"],'')
                        self.tiles.add(tile)
                    case'32':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["IceyCorner"],'')
                        self.tiles.add(tile)
                    case'33':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["IceyWall"],'')
                        self.tiles.add(tile)
                    case'34':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelUnderFloor"],'')
                        self.tiles.add(tile)
                    case'35':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelWall"],'')
                        self.tiles.add(tile)
                    case'36':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelCorner"],'')
                        self.tiles.add(tile)
                    case'37':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["MagmaSpurt"],'')
                        self.tiles.add(tile)
                    case'38':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["DrakeCeiling"],'')
                        self.tiles.add(tile)
                    case'39':
                        tile = StaticTile(TILESIZE,x,y,GAMETILES["ChapelCeiling"],'')
                        self.tiles.add(tile)

    def cameraScroll(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x
        if playerX <= (WINDOWSIZE[0]/2)/self.playerToScreenOffset and directionX < 0:
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
        #dust particles
        self.dustSprite.update(self.worldShift)
        self.dustSprite.draw(self.displaySurface)
            
        #Map Tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.cameraScroll()
        
        #player
        self.player.update()
        self.horizontalCollision()
        self.groundedCheck()
        self.verticalCollision()
        self.player.draw(self.displaySurface)
        
        #decoration
        # self.sky.draw(self.displaySurface)

        #landing particles
        # self.createLandingParticle()