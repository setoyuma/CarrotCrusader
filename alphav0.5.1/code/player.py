import pygame as pg, sys 
from support import import_folder
from settings import *

class Player(pg.sprite.Sprite):
	def __init__(self,pos,surface,create_jump_particles):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0
		self.image = self.animations['idle'][self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)
		self.animation_speed = 0.20	

		# dust particles 
		self.import_dust_run_particles()
		self.dust_frame_index = 0
		self.dust_animation_speed = 0.18
		self.display_surface = surface
		self.create_jump_particles = create_jump_particles

		# player movement
		self.direction = pg.math.Vector2(0,0)
		self.speed = 6
		self.gravity = 0.5
		self.jump_speed = -13.5

		#respawn
		self.spawnX = pos[0]
		self.spawnY = pos[1]
		
		# player status
		self.status = 'idle'
		self.facing_right = True
		self.on_ground = False
		self.on_ceiling = False
		self.on_left = False
		self.on_right = False
		self.hitBoxOn = False

		#health mgmt
		self.hitStatus = False
		self.hp = 100
		self.invincible = False
		self.invincibilityDuration = 800
		self.hurtTime = 0


		#attacks
		self.groundAttack = False
		self.attackBox = pg.rect.Rect(screen_width,screen_height,0,0)

	def import_character_assets(self):
		character_path = '../graphics/character/'
		self.animations = {'idle':[],'run':[],'jump':[],'fall':[],'attack':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def import_dust_run_particles(self):
		self.dust_run_particles = import_folder('../graphics/character/dust_particles/run')

	def animate(self):
		animation = self.animations[self.status]
		self.hitBox = pg.rect.Rect(self.rect.x,self.rect.y,38,64)
		self.hitBox.center = self.rect.center
		# loop over frame index 
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		image = animation[int(self.frame_index)]
		if self.facing_right:
			self.image = image
		else:
			flipped_image = pg.transform.flip(image,True,False)
			self.image = flipped_image

		# set the rect
		if self.on_ground and self.on_right:
			# self.rect = self.hitBox
			self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
		elif self.on_ground and self.on_left:
			# self.rect = self.hitBox
			self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
		elif self.on_ground:
			# self.rect = self.hitBox
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
		elif self.on_ceiling and self.on_right:
			# self.rect = self.hitBox
			self.rect = self.image.get_rect(topright = self.rect.topright)
		elif self.on_ceiling and self.on_left:
			# self.rect = self.hitBox
			self.rect = self.image.get_rect(topleft = self.rect.topleft)
		elif self.on_ceiling:
			# self.rect = self.hitBox
			self.rect = self.image.get_rect(midtop = self.rect.midtop)

	def run_dust_animation(self):
		if self.status == 'run' and self.on_ground:
			self.dust_frame_index += self.dust_animation_speed
			if self.dust_frame_index >= len(self.dust_run_particles):
				self.dust_frame_index = 0

			dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

			if self.facing_right:
				pos = self.rect.bottomleft - pg.math.Vector2(6,10)
				self.display_surface.blit(dust_particle,pos)
			else:
				pos = self.rect.bottomright - pg.math.Vector2(6,10)
				flipped_dust_particle = pg.transform.flip(dust_particle,True,False)
				self.display_surface.blit(flipped_dust_particle,pos)

	def showHitbox(self,target):
		self.hitBoxOn = True
		pg.draw.rect(self.display_surface,'blue',target.rect)
		pg.draw.rect(self.display_surface,'green',target.hitBox)

	def get_input(self):
		keys = pg.key.get_pressed()

		if keys[pg.K_d]:
			self.direction.x = 1
			self.facing_right = True
		elif keys[pg.K_a]:
			self.direction.x = -1
			self.facing_right = False
		else:
			self.direction.x = 0

		if keys[pg.K_SPACE] and self.on_ground:
			self.jump()
			self.create_jump_particles(self.rect.midbottom)

		if keys[pg.K_h]:
			self.showHitbox(self)
		else:
			self.hitBoxOn = False

		if keys[pg.K_p]:
			font = pg.font.Font(None,64)
			text = font.render("Ground Attack",False,'white','black')
			textPos = text.get_rect(centerx=self.display_surface.get_width()/2, y=10)
			self.display_surface.blit(text,textPos)

			'''make atk hitbox'''
			self.groundAttack = True
			if self.facing_right:
				self.attackBox = pg.rect.Rect((self.rect.right-50),(self.rect.top+20),50,30)
				self.rect.union(self.attackBox)
				# pg.draw.rect(self.display_surface,'red',self.attackBox,0,-1,-1,5,-1,5)
			
			elif self.facing_right == False:
				self.attackBox = pg.rect.Rect((self.rect.right-50),(self.rect.top+20),-50,30)
				self.rect.union(self.attackBox)
				# pg.draw.rect(self.display_surface,'red',self.attackBox,0,-1,5,-1,5,-1)
		else:
			self.groundAttack = False
			self.attackBox = pg.rect.Rect(0,0,0,0)

		

	def get_status(self):
		if self.direction.y < 0:
			self.status = 'jump'
		elif self.direction.y > 1 and self.on_ground == False:
			self.status = 'fall'
		elif self.direction.x != 0 and self.on_ground:
			self.status = 'run'
		else:
			if self.direction.y == 0 and self.on_ground:
				self.status = 'idle'

		if self.groundAttack:
			self.status = 'attack'
			if self.on_ground:
				self.speed = 0
			else:
				self.speed = 4


	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jump_speed

	def getDamage(self):
		if not self.invincible:
			self.hp -= 10
			self.invincible = True
			self.hurtTime = pg.time.get_ticks()

	def iFrameTimer(self):
		if self.invincible:
			currentTime = pg.time.get_ticks()
			if currentTime - self.hurtTime >= self.invincibilityDuration:
				self.invincible = False

	def update(self):
		# pg.draw.rect(self.display_surface,'pink',self.attackBox)

		#respawn
		# if self.rect.y > 714:
		# 	print(self.rect.y)
		# 	self.rect.x = self.spawnX + self.rect.x
		# 	self.rect.y = self.spawnY 

		self.get_input()
		self.get_status()
		self.animate()
		self.run_dust_animation()
		self.iFrameTimer()
		# print('player rect y: ',self.rect.y,'\n')
		# print('player rect x: ',self.rect.x,'\n')
		