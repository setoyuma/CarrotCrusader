import pygame as pg
from support import importFolder


class Tile(pg.sprite.Sprite):
    def __init__(self,pos,img,isAnim=False):
        super().__init__()
        self.importAssets()
        self.frameIndex = 0
        self.animationSpeed = 0.25
        match isAnim:
            case False:
                self.image = img
            case True:
                print(isAnim)
                self.image = self.animations['Magmapool'][self.frameIndex]
                self.animate()
        # self.image = pg.image.load('../assets/tiles/Classic.png')
        # self.image = pg.image.load('../assets/tiles/ATOT/CTOS_Floor.png')
        # self.image = pg.Surface((size,size))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

    def importAssets(self):
        animPath = '../assets/tiles/AnimTiles/'
        self.animations = {
            'Magmapool': [],
            'Non': [],
        }
        

        for animation in self.animations.keys():
            fullPath =animPath + animation
            self.animations[animation] = importFolder(fullPath)

    def animate(self):
        animation = self.animations['Magmapool']

        #loop over frame index
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0

        self.image = animation[int(self.frameIndex)]

    def update(self,xShift):
        self.rect.x += xShift
        # self.animate()