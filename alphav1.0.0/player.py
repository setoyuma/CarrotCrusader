import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,groups,collisionSprites):
        super().__init__(groups)
        self.image = pg.Surface((TILE_SIZE//2,TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=pos)

        #player movement
        self.direction = pg.math.Vector2()
        self.speed = 6
        self.gravity = 0.8
        self.jumpHeight = 15  #jump speed
        self.collisionSprites = collisionSprites
        self.onGround = False

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_d]:
            self.direction.x = 1
        elif keys[pg.K_a]:
            self.direction.x = -1
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

