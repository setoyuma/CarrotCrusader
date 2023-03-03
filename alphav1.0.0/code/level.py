import pygame as pg
from settings import *
from tile import Tile,StaticTile
from player import Player
from support import *
from ui import UI
from camera import CameraGroup


class Level:

    def __init__(self,level_data):
        #level setup
        self.displaySurface = pg.display.get_surface()

        # ui
        self.UI = UI(self.displaySurface)

        #sprite group setup
        self.visibleSprites = CameraGroup()  #sprites here will be drawn
        self.activeSprites = pg.sprite.Group() # sprites in here will be updated
        self.collisionSprites = pg.sprite.Group() #sprites that the player can collide with

        #terrain layout
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')
        
        # player 
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)



 
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
                            sprite = Tile(TILE_SIZE,)
                        
                        sprite_group.add(sprite)
                        
        return sprite_group

    def player_setup(self,layout):
         for row_index, row in enumerate(layout):
              for col_index,val in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if val == '0':
                    # print(f"Proper Spawn x: {x}")
                    # print(f"Proper Spawn y: {y}")
                    self.Player = Player((x,y),[self.visibleSprites,self.activeSprites],self.collisionSprites,self.displaySurface)
                    self.player.add(self.Player)
                if val == '1':
                    hat_surface = pygame.image.load('../graphics/character/hat.png').convert_alpha()
                    sprite = Tile((x,y),[self.activeSprites])
                    self.goal.add(sprite)

    def run(self):
        #run the game(level)
        self.player.update()
        self.visibleSprites.customDraw(self.Player)

        #ui
        self.UI.show_health(self.Player.hp,100)


    