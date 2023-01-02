import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,groups,collideSprites) -> None:
        super().__init__(groups)
        self.image = pg.image.load('./imgs/vegnath/vegnath0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.direction = pg.math.Vector2()
        self.speed = 3

        self.collideSprites = collideSprites

    def playerInput(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            self.direction.y -= 1
        elif keys[pg.K_s]:
            self.direction.y += 1
        else:
            self.direction.y = 0

        if keys[pg.K_d]:
            self.direction.x += 1
        elif keys[pg.K_a]:
            self.direction.x -= 1
        else:
            self.direction.x = 0

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        # self.rect.center += self.direction * speed

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.collideSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.collideSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.playerInput()
        self.move(self.speed)