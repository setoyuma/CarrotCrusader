import pygame as pg 
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
	def __init__(self,size,x,y,surf,type):
		super().__init__(size,x,y,f'../graphics/enemy/{type}/run')
		self.rect.y += size - self.image.get_size()[1]
		# self.rect = self.image.get_rect()
		self.speed = 2
		self.displaySurface = surf
		
		# self.speed = randint(3,5)

	def move(self):
		self.rect.x += self.speed

	def reverse_image(self):
		if self.speed > 0:
			self.image = pg.transform.flip(self.image,True,False)

	def reverse(self):
		self.speed *= -1

	def update(self,shiftx,shifty):
		self.hitBox = pg.rect.Rect(self.rect.x,self.rect.y,38,64)
		self.hitBox.center = self.rect.center
		self.hitBox.inflate_ip(-13.5,10)
		# self.rect = self.hitBox
		self.rect.x += shiftx
		self.rect.y += shifty
		self.animate()
		self.move()
		self.reverse_image()

		#show hitbox
		# pg.draw.rect(self.displaySurface,'purple',self.hitBox)
		# pg.draw.rect(self.displaySurface,'red',self.rect)
		