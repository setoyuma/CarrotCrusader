import pygame as pg, sys
from debug import debug
from support import importFolder
from pygame.locals import * 
# i put this here in nvim
#lmao my balls itch


# use anim func from player in level class to render anim tiles with smaller dict




class Player(pg.sprite.Sprite):
    def __init__(self,pos,surf):
        super().__init__()
        self.importAssets()
        self.displaySurface = surf
        self.animationSpeed = 0.20
        self.frameIndex = 0
        self.image = self.animations['Idle'][self.frameIndex]
        self.rect = pg.rect.Rect(pos[0],pos[1],22,29)
        # self.rect.inflate_ip(-15,0)
        # self.rect = self.image.get_rect(center=pos)
        # self.rect = pg.Rect.inflate_ip(self.rect,(-15,0))

        #player movement
        self.direction = pg.math.Vector2(0,0)
        self.speed = 3
        self.gravity = 0.8
        self.jumpSpeed = -10
        self.airBorne = False

    def importAssets(self):
        animPath = '../assets/Player/Alryn/'
        self.animations = {
            'Idle': [],
            'Run': [],
            'Jump': [],
            'Fall': [],
        }

        for animation in self.animations.keys():
            fullPath =animPath + animation
            self.animations[animation] = importFolder(fullPath)

    def animate(self):
        animation = self.animations['Idle']

        #loop over frame index
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0

        self.image = animation[int(self.frameIndex)]
    
    def showHitBoxes(self, surf, target):
        pg.draw.rect(surf,'limeGreen',target.rect)


    def getInput(self,surf):
        keys = pg.key.get_pressed()
        surf = surf

        if keys[pg.K_d]:
            self.direction.x = 1
        elif keys[pg.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pg.K_SPACE]:
            self.jump()

        if keys[pg.K_h]:
            print('hitbox view')
            self.showHitBoxes(surf,self)

        

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.airBorne == False:
            self.airBorne = True
            self.direction.y = self.jumpSpeed
        else:
            self.direction.y = self.direction.y


    def update(self):
        self.getInput(self.displaySurface)
        self.animate()
