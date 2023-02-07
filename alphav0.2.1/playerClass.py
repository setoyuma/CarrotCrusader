import pygame as pg, sys
from debug import debug
from support import importFolder
from pygame.locals import * 
# i put this here in nvim

class Player(pg.sprite.Sprite):
    def __init__(self,pos,surf):

        super().__init__()
        self.importAssets()
        self.displaySurface = surf
        self.animationSpeed = .3
        self.frameIndex = 0
        self.image = self.animations['Idle'][self.frameIndex]
        self.rect = pg.rect.Rect(pos[0],pos[1],22,29)
        # self.rect.inflate_ip(-15,0)
        # self.rect = self.image.get_rect(center=pos)
        # self.rect = pg.Rect.inflate_ip(self.rect,(-15,0))

        #player movement
        self.direction = pg.math.Vector2(0,0)
        self.speed = 2
        self.gravity = 0.8
        self.jumpSpeed = -10
        self.airBorne = False
        
        #player status
        self.status = 'Idle'
        self.facingRight = True

    def importAssets(self):
        animPath = '../assets/Player/'
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
        animation = self.animations[self.status]

        #loop over frame index
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0
        
        image = self.image = animation[int(self.frameIndex)]
        if self.facingRight:
            self.image = image
        else:
            flippedImage = pg.transform.flip(image, True, False)
            self.image = flippedImage
              
    def showHitBoxes(self, surf, target):
        pg.draw.rect(surf,'limeGreen',target.rect)

    def getInput(self,surf):
        keys = pg.key.get_pressed()
        surf = surf

        #player flip code
        # if self.direction.x < 0:
        #     self.image = pg.transform.flip(self.image,True,False)


        
        if keys[pg.K_d]:
            self.direction.x = 1
            self.facingRight = True
        elif keys[pg.K_a]:
            self.direction.x = -1
            self.facingRight = False
        else:
            self.direction.x = 0

        if keys[pg.K_SPACE]:
            self.jump()

        if keys[pg.K_h]:
            print('hitbox view')
            self.showHitBoxes(surf,self)

    def getState(self):
        if self.direction.y < 0:
            self.status = 'Jump'
        # elif self.direction.y > .7:
        #     self.status = 'Fall'
        else:
            if self.direction.x != 0:
                self.status = 'Run'
            else:
                self.status = 'Idle'

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
        self.getState()
        self.animate()

