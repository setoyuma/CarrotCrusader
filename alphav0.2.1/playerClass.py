import pygame as pg, sys
from debug import debug
from support import importFolder
from pygame.locals import * 
# i put this here in nvim

class Player(pg.sprite.Sprite):
    def __init__(self,pos,surf,createJumpParticle):
        super().__init__()
        self.importAssets()
        self.displaySurface = surf
        self.animationSpeed = .25
        self.frameIndex = 0
        self.image = self.animations['Idle'][self.frameIndex]
        self.rect = pg.rect.Rect(pos[0],pos[1],22,29)
        # self.rect.inflate_ip(-15,0)
        # self.rect = self.image.get_rect(center=pos)
        # self.rect = pg.Rect.inflate_ip(self.rect,(-15,0))
        
        #dust particles
        self.importRunParticles()
        self.dustanimationSpeed = .3
        self.dustFrameIndex = 0
        self.createJumpParticle = createJumpParticle
        
        #player movement
        self.direction = pg.math.Vector2(0,0)
        self.speed = .8
        self.gravity = 0.4
        self.jumpSpeed = -7
        self.airBorne = False
        self.wallJumps = 0

        #player stats
        self.hitpoints = 100

        #player status
        self.status = 'Idle'
        self.facingRight = True
        self.onGround = False
        self.onCeiling = False
        self.onLeftWall = False
        self.onRightWall = False

    def importAssets(self):
        animPath = '../assets/Player/'
        self.animations = {
            'Idle': [],
            'Run': [],
            'Jump': [],
            'Fall': [],
            'WallJump': [],
            'Damage': [],
        }

        for animation in self.animations.keys():
            fullPath = animPath + animation
            self.animations[animation] = importFolder(fullPath)

    def importRunParticles(self):
        self.runParticles = importFolder('../assets/dust_particles/run')

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
              
        #set rect
        if self.onGround and self.onRightWall:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.onGround and self.onLeftWall:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.onGround:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        
        elif self.onCeiling and self.onRightWall:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.onCeiling and self.onLeftWall:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.onCeiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def runningParticlesAnimator(self):
        if self.status == "Run" and self.onGround:
            self.dustFrameIndex += self.dustanimationSpeed
            if self.dustFrameIndex >= len(self.runParticles):
                self.dustFrameIndex = 0

            dustParticle = self.runParticles[int(self.dustFrameIndex)]

            if self.facingRight:
                pos = self.rect.bottomleft - pg.math.Vector2(6,10)
                self.displaySurface.blit(dustParticle,pos)
            else:
                pos = self.rect.bottomright - pg.math.Vector2(6,10)
                flippedDustParticle = pg.transform.flip(dustParticle,True,False)
                self.displaySurface.blit(flippedDustParticle,pos)

    def showHitBoxes(self, surf, target):
        pg.draw.rect(surf,'limeGreen',target.rect)

    def getInput(self,surf):
        keys = pg.key.get_pressed()
        surf = surf

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

        '''SHOW HITBOX/RECT'''
        if keys[pg.K_h]:
            print('hitbox view')
            self.showHitBoxes(surf,self)

    def getState(self):
        if self.direction.y < 0:
            self.status = 'Jump'
        elif self.direction.y > .9:
            self.status = 'Fall'
        else:
            if self.direction.x != 0 and self.onGround:
                self.status = 'Run'
            else:
                self.status = 'Idle'

        # '''WALLJUMP STATE'''
        # if self.onGround == False and self.direction.y >= -4:
        #     if self.onLeftWall:
        #         self.status = 'WallJump'
        # if self.onGround == False and self.direction.y >= -4:
        #     if self.onRightWall:
        #         self.status = 'WallJump'
            
    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.airBorne == False:
            self.airBorne = True
            self.direction.y = self.jumpSpeed
        
        # '''WALLJUMP EXECUTION (currently scuffed asf)'''
        # if self.status =="WallJump" and self.onLeftWall and self.onGround == False and self.wallJumps:
        #         self.wallJumps -= 1
        #         self.direction.y = self.jumpSpeed
        #         # self.rect.x + 70
        # if self.status =="WallJump" and self.onRightWall and self.onGround == False and self.wallJumps:
        #         self.wallJumps -= 1
        #         self.direction.y = self.jumpSpeed
        #         # self.direction.x + 70

        else:
            self.direction.y = self.direction.y
            if self.onGround and self.wallJumps == 0:
                self.wallJumps += 1
                print(self.wallJumps)

    def respawn(self, pos):
        self.rect.y,self.rect.x = pos

    def update(self):
        self.getInput(self.displaySurface)
        self.getState()
        self.animate()
        self.runningParticlesAnimator()
