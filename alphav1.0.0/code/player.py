import pygame as pg
from settings import *
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,groups,collisionSprites,surface):
        super().__init__(groups)
        self.import_character_assets()
        self.image = pg.Surface((TILE_SIZE//2,TILE_SIZE))
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # dust particles 
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.20
        self.display_surface = surface
        # self.create_jump_particles = create_jump_particles

        #player stats
        self.hp = 100

        #player state
        self.animation_speed = 0.15
        self.status = 'idle'
        self.on_left = False
        self.on_right = False
        self.hitBoxOn = False

        #player movement
        self.direction = pg.math.Vector2()
        self.speed = 6
        self.gravity = 0.65
        self.jumpHeight = 15  #jump speed
        self.collisionSprites = collisionSprites
        self.onGround = False
        self.onCeiling = False
        self.facing_right = True


    def import_character_assets(self):
        character_path = '../graphics/character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[],'attack':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]
        self.hitBox = pg.rect.Rect(self.rect.x,self.rect.y,38,64)
        self.hitBox.center = self.rect.center
		# loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pg.transform.flip(image,True,False)
            self.image = flipped_image

		# set the rect
        if self.onGround and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.onGround and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.onGround:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.onCeiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.onCeiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.onCeiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('../graphics/character/dust_particles/run')

    def run_dust_animation(self):
        if self.status == 'run' and self.onGround:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pg.math.Vector2(6,10)
                self.display_surface.blit(dust_particle,pos)
            else:
                pos = self.rect.bottomleft - pg.math.Vector2(6,10)
                flipped_dust_particle = pg.transform.flip(dust_particle,True,False)
                self.display_surface.blit(flipped_dust_particle,pos)
                
    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1 and self.onGround == False:
             self.status = 'fall'
        elif self.direction.x != 0 and self.onGround:
             self.status = 'run'
        else:
             if self.direction.y == 0 and self.onGround:
                 self.status = 'idle'

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_d]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pg.K_a]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pg.K_SPACE] and self.onGround:
            self.direction.y = -self.jumpHeight

    def horizontalCollisions(self):
        for sprite in self.collisionSprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def verticalCollisions(self):
        for sprite in self.collisionSprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.onGround = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

            if self.onGround and self.direction.y != 0:
                self.onGround = False
    
    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontalCollisions()
        self.applyGravity()
        self.verticalCollisions()

        self.get_status()
        self.animate()
        # self.run_dust_animation()

        # pg.draw.rect(self.display_surface,'red',self.rect)
        # pg.draw.rect(self.display_surface,'red',self.hitBox)
