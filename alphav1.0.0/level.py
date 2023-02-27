import pygame as pg
from settings import *
from tile import Tile
from player import Player


class Level:

    def __init__(self):
        #level setup
        self.displaySurface = pg.display.get_surface()

        #sprite group setup
        self.visibleSprites = CameraGroup()  #sprites here will be drawn
        self.activeSprites = pg.sprite.Group() # sprites in here will be updated
        self.collisionSprites = pg.sprite.Group() #sprites that the player can collide with

        self.setupLevel()

    def create_tile_group(self,layout,type):
		sprite_group = pygame.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val != '-1':
					x = col_index * tile_size
					y = row_index * tile_size

					if type == 'terrain':
						terrain_tile_list = import_cut_graphics('../graphics/terrain/terrain_tiles.png')
						tile_surface = terrain_tile_list[int(val)]
						sprite = StaticTile(tile_size,x,y,tile_surface)

					if type == 'caim':
						sprite = Enemy(tile_size,x,y,'caim')
					if type == 'mossSent':
						sprite = Enemy(tile_size,x,y,'mossSent')

					if type == 'constraint':
						sprite = Tile(tile_size,x,y)

					sprite_group.add(sprite)
		
		return sprite_group

    def setupLevel(self):
        for rowIndex,row in enumerate(LEVEL_MAP):
            # print(f'{rowIndex}: {row}')
            for colIndex,col in enumerate(row):
                # print(f'{colIndex}: {col}')
                x = colIndex * TILE_SIZE
                y = rowIndex*TILE_SIZE

                match col:
                    case 'X':
                        Tile((x,y),[self.visibleSprites,self.collisionSprites])
                    case 'P':
                        self.player = Player((x,y),[self.visibleSprites,self.activeSprites],self.collisionSprites)

    def run(self):
        #run the game(level)
        self.activeSprites.update()
        self.visibleSprites.customDraw(self.player)


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

    