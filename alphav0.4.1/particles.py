import pygame as pg
from support import importFolder

class ParticleEffect(pg.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.frameIndex = 0

        self.animationSpeed = .5

        if type == "Jump":
            self.frames = importFolder('../assets/dust_particles/jump')
        if type == "Land":
            self.frames = importFolder('../assets/dust_particles/land')
        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect(center=pos)


    def animate(self):
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frameIndex)]

    def update(self,xShift):
        self.animate()
        self.rect.x += xShift
