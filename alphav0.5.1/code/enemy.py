import pygame 
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
	def __init__(self,size,x,y,enemy_type):
		super().__init__(size,x,y,f'../graphics/enemy/{enemy_type}/run')
		self.rect.y += size - self.image.get_size()[1]
		
		if enemy_type == 'caim':
			self.speed = 5
		
		if enemy_type == 'mossSent':
			self.speed = 3

	def move(self):
		self.rect.x += self.speed

	def reverse_image(self):
		if self.speed > 0:
			self.image = pygame.transform.flip(self.image,True,False)

	def reverse(self):
		self.speed *= -1

	def update(self,shiftx,shifty):
		self.rect.x += shiftx
		self.rect.y += shifty
		self.animate()
		self.move()
		self.reverse_image()