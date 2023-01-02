import pygame as pg
from settingsR import *
from sprite import Sprite

class Player(Sprite):

    def __init__(self) -> None:
        Sprite.__init__(self)
        self.moving_right = False
        self.moving_left = False
        self.vertical_momentum = 0
        self.air_timer = 0
        self.player_action = 'idle'
        self.player_frame = 0
        self.player_flip = False
        self.player_rect = pg.Rect(100,100,5,13)
        self.player_movement = [0,0]


    def collisionTest(self,rect,tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self,rect,movement,tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        rect.x += movement[0]
        hit_list = self.collisionTest(rect,tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = self.collisionTest(rect,tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def moveCheck(self):
        if self.moving_right == True:
            self.player_movement[0] += 2
        if self.moving_left == True:
            self.player_movement[0] -= 2
        self.player_movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 3

        if self.player_movement[0] == 0:
            self.player_action,self.player_frame = self.changeAction(self.player_action,self.player_frame,'idle')
        if self.player_movement[0] > 0:
            self.player_flip = False
            self.player_action,self.player_frame = self.changeAction(self.player_action,self.player_frame,'run')
        if self.player_movement[0] < 0:
            self.player_flip = True
            self.player_action,self.player_frame = self.changeAction(self.player_action,self.player_frame,'run')

        self.player_rect,self.collisions = self.move(self.player_rect,self.player_movement,tileRects)

        if self.collisions['bottom'] == True:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1
    

    def animate(self,surf):

        self.player_frame += 1
        if self.player_frame >= len(self.animation_database[self.player_action]):
            self.player_frame = 0
        self.player_img_id = self.animation_database[self.player_action][self.player_frame]
        self.player_img = self.animationFrames[self.player_img_id]
        surf.blit(pg.transform.flip(self.player_img,self.player_flip,False),(self.player_rect.x-scroll[0],self.player_rect.y-scroll[1]))


