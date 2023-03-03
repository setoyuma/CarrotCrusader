import pygame as pg
from settings import *


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
        '''CENTER CAM'''
        # #get player offset
        # self.offset.x = player.rect.centerx - self.halfWidth
        # self.offset.y = player.rect.centery - self.halfHeight

        '''BOX CAM'''
        #get camera pos
        if player.rect.left < self.cameraRect.left:
            self.cameraRect.left = player.rect.left
        
        if player.rect.right > self.cameraRect.right:
            self.cameraRect.right = player.rect.right
        
        if player.rect.top < self.cameraRect.top:
            self.cameraRect.top = player.rect.top
        
        if player.rect.bottom > self.cameraRect.bottom:
            self.cameraRect.bottom = player.rect.bottom

        # camera offset
        self.offset = pg.math.Vector2(
            self.cameraRect.left - CAMERA_BORDERS['left'],
            self.cameraRect.top - CAMERA_BORDERS['top'])

        for sprite in self.sprites():
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image,offsetPos)

        # pg.draw.rect(self.displaySurface,'red',self.cameraRect)