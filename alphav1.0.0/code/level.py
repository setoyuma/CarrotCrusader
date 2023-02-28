import pygame as pg
from settings import *
from tile import Tile,StaticTile
from player import Player
from support import *
from ui import UI


class Level:

    def __init__(self,level_data):
        #level setup
        self.displaySurface = pg.display.get_surface()

        #sprite group setup
        self.visibleSprites = CameraGroup()  #sprites here will be drawn
        self.activeSprites = pg.sprite.Group() # sprites in here will be updated
        self.collisionSprites = pg.sprite.Group() #sprites that the player can collide with

        # ui
        self.UI = UI(self.displaySurface)
        # player 
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        #terrain layout
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

    def create_tile_group(self,layout,type):
        sprite_group = pg.sprite.Group()

        for row_index, row in enumerate(layout):
                for col_index,val in enumerate(row):
                    if val != '-1':
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE
                        
                        if type == 'terrain':
                            terrain_tile_list = import_cut_graphics('../levels/tilesets/staticTiles.png')
                            tile_surface = terrain_tile_list[int(val)]
                            sprite = StaticTile((x,y),[self.visibleSprites,self.collisionSprites],tile_surface)
                        if type == 'constraint':
                            sprite = Tile(TILE_SIZE,x,sprite_group.add(sprite))
        return sprite_group

    def player_setup(self,layout):
         for row_index, row in enumerate(layout):
              for col_index,val in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if val == '0':
                    self.Player = Player((x,y),[self.visibleSprites,self.activeSprites],self.collisionSprites,self.displaySurface)
                    self.player.add(self.Player)
                if val == '1':
                    hat_surface = pygame.image.load('../graphics/character/hat.png').convert_alpha()
                    sprite = Tile((x,y),[self.activeSprites])
                    self.goal.add(sprite)

    def run(self):
        #run the game(level)
        #player
        self.activeSprites.update()
        self.visibleSprites.customDraw(self.Player)

        #ui
        self.UI.show_health(self.Player.hp,100)


class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pg.display.get_surface()
        self.offset = pg.math.Vector2(100,300)

        #center camera setup
        self.halfWidth = self.displaySurface.get_size()[0]//2
        self.halfHeight = self.displaySurface.get_size()[1]//2

        #camera box
        camLeft = CAMERA_BORDERS['left']
        camTop = CAMERA_BORDERS['top']
        camWidth = self.displaySurface.get_size()[0] - (camLeft + CAMERA_BORDERS['right'])
        camHeight = self.displaySurface.get_size()[1] - (camTop + CAMERA_BORDERS['bottom'])

        self.cameraRect = pg.Rect(camLeft,camTop,camWidth,camHeight)

    def customDraw(self,player):
        # #get player offset
        # self.offset.x = player.rect.centerx - self.halfWidth
        # self.offset.y = player.rect.centery - self.halfHeight

        #get camera pos
        if player.rect.left < self.cameraRect.left:
            self.cameraRect.left = player.rect.left
        
        if player.rect.right > self.cameraRect.right:
            self.cameraRect.right = player.rect.right
        
        if player.rect.top < self.cameraRect.top:
            self.cameraRect.top = player.rect.top
        
        if player.rect.bottom > self.cameraRect.bottom:
            self.cameraRect.bottom = player.rect.bottom

        #camera offset
        self.offset = pg.math.Vector2(
            self.cameraRect.left - CAMERA_BORDERS['left'],
            self.cameraRect.top - CAMERA_BORDERS['top'])

        for sprite in self.sprites():
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image,offsetPos)

        # pg.draw.rect(self.displaySurface,'red',self.cameraRect)

    