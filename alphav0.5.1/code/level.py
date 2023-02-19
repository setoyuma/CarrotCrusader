import pygame as pg 
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height, screen_width
from tiles import Tile, StaticTile, Crate, Coin, Palm
from enemy import Enemy
from decoration import Sky
from player import Player
from particles import ParticleEffect
from ui import UI
from game_data import levels
from Camera import Camera


class Level:
	def __init__(self,level_data,surface):
		# general setup
		self.display_surface = surface
		self.world_shiftx = 0
		self.world_shifty = 0
		self.current_x = None
		self.gameLevels = levels
		self.currentLevel = 0
		self.level_data = level_data

		#camera
		self.camera = Camera()

		# player 
		player_layout = import_csv_layout(self.level_data['player'])
		self.playerSpriteGroup = pg.sprite.GroupSingle()
		self.goal = pg.sprite.GroupSingle()
		self.goBack = pg.sprite.GroupSingle()
		self.player_setup(player_layout)

		#UI
		self.UI = UI(self.display_surface)

		# dust 
		self.dust_sprite = pg.sprite.GroupSingle()
		self.player_on_ground = False

		# explosion particles 
		self.explosion_sprites = pg.sprite.Group()

		# terrain setup
		terrain_layout = import_csv_layout(self.level_data['terrain'])
		self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

		# background pillars 
		bg_pillar_layout = import_csv_layout(self.level_data['bg Pillar'])
		self.bg_pillar_sprites = self.create_tile_group(bg_pillar_layout,'bg Pillar')

		# enemy 
		enemy_layout = import_csv_layout(self.level_data['enemies'])
		self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

		# constraint 
		constraint_layout = import_csv_layout(self.level_data['constraints'])
		self.constraint_sprites = self.create_tile_group(constraint_layout,'constraint')

		# decoration 
		# self.sky = Sky(0)
		level_width = len(terrain_layout[0]) * tile_size

	def create_tile_group(self,layout,type):
		sprite_group = pg.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val != '-1':
					x = col_index * tile_size
					y = row_index * tile_size

					if type == 'terrain':
						terrain_tile_list = import_cut_graphics('../graphics/terrain/terrain_tiles.png')
						tile_surface = terrain_tile_list[int(val)]
						sprite = StaticTile(tile_size,x,y,tile_surface)
						
					if type == 'bg Pillar':
						sprite = Palm(tile_size,x,y,'../graphics/terrain/bg_pillar',64)

					if type == 'enemies':
						sprite = Enemy(tile_size*3,x,y,self.display_surface,'RockSentinel')   #change enemy hitbox

					if type == 'constraint':
						sprite = Tile(tile_size,x,y)

					sprite_group.add(sprite)
		
		return sprite_group

	def player_setup(self,layout):
		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				if val == '0':
					self.Player = Player((x,y),self.display_surface,self.create_jump_particles)
					self.playerSpriteGroup.add(self.Player)
				if val == '1':
					hat_surface = pg.image.load('../graphics/character/hat.png').convert_alpha()
					sprite = StaticTile(tile_size,x,y,hat_surface)
					self.goal.add(sprite)
				if val == '2':
					hat_surface = pg.image.load('../graphics/character/hat.png').convert_alpha()
					sprite = StaticTile(tile_size,x,y,hat_surface)
					self.goBack.add(sprite)

	def enemy_collision_reverse(self):
		for enemy in self.enemy_sprites.sprites():
			if pg.sprite.spritecollide(enemy,self.constraint_sprites,False):
				enemy.reverse()

	def check_enemy_collisions(self,target):
				for enemy in self.enemy_sprites.sprites():
					enemy_center = enemy.hitBox.centery
					enemy_top = enemy.hitBox.top
					player_bottom = target.hitBox.bottom
					if pg.Rect.colliderect(enemy.hitBox, target.hitBox):
						if enemy_top < player_bottom < enemy_center and target.direction.y >= 0:
							# self.stomp_sound.play()
							target.direction.y = -15
							explosion_sprite = ParticleEffect(enemy.hitBox.center,'explosion')
							self.explosion_sprites.add(explosion_sprite)
							enemy.kill()
						else:	#player damage step
							target.getDamage()


	def enemyGotHit(self,target):
		for enemy in self.enemy_sprites.sprites():
			if target.groundAttack and pg.Rect.colliderect(target.attackBox,enemy.hitBox):
				print('enemy hit by player attack')

			else:
				pass


	# def enemyHit(self,target):
	# 	for enemy in self.enemy_sprites.sprites():
	# 		if pg.Rect.colliderect(enemy.hitBox, target.hitBox):
	# 			target.hitStatus = True
	# 			target.rect.x -= 85
	# 			target.rect.y -= 15
	# 			print('\nplayer hit\n')
	# 			self.Player.hp -= 10
	# 			# target.rect.x -= 1   #possible mvmnt slow

	def create_jump_particles(self,pos):
		if self.playerSpriteGroup.sprite.facing_right:
			pos -= pg.math.Vector2(10,5)
		else:
			pos += pg.math.Vector2(10,-5)
		jump_particle_sprite = ParticleEffect(pos,'jump')
		self.dust_sprite.add(jump_particle_sprite)

	def horizontal_movement_collision(self):
		player = self.playerSpriteGroup.sprite
		player.rect.x += player.direction.x * player.speed
		collidable_sprites = self.terrain_sprites.sprites()
		for sprite in collidable_sprites:
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False

	def vertical_movement_collision(self):
		player = self.playerSpriteGroup.sprite
		player.apply_gravity()
		collidable_sprites = self.terrain_sprites.sprites()

		for sprite in collidable_sprites:
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			player.on_ceiling = False

	def scroll_x(self):
		player = self.playerSpriteGroup.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < self.camera.camera_rect.left + (screen_width / 4) and direction_x < 0:
		# if player_x < screen_width / 4 and direction_x < 0:
			self.world_shiftx = 5
			player.speed = 0
		elif player_x > self.camera.camera_rect.right - (screen_width / 4) and direction_x > 0:
		# elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.world_shiftx = -5
			player.speed = 0
		else:
			self.world_shiftx = 0
			player.speed = 5
	
	# def scroll_y(self):
	# 	player = self.Player
	# 	if player.rect.y < (screen_height/3):
	# 		print('scroll down')
	# 		self.world_shifty = 5
	# 		player.rect.y  -= 5
	# 	elif player.rect.y > (screen_height-100):
	# 		print('scroll up')
	# 		self.world_shifty = -5
	# 		player.rect.y  += 5
	# 	else:
	# 		self.world_shifty = 0
			

	def get_player_on_ground(self):
		if self.playerSpriteGroup.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False

	def create_landing_dust(self):
		if not self.player_on_ground and self.playerSpriteGroup.sprite.on_ground and not self.dust_sprite.sprites():
			if self.playerSpriteGroup.sprite.facing_right:
				offset = pg.math.Vector2(10,15)
			else:
				offset = pg.math.Vector2(-10,15)
			fall_dust_particle = ParticleEffect(self.playerSpriteGroup.sprite.rect.midbottom - offset,'land')
			self.dust_sprite.add(fall_dust_particle)

	def run(self):
		# run the entire game / level 
		
		# sky 
		# self.sky.draw(self.display_surface)
		
		# background palms
		self.bg_pillar_sprites.update(self.world_shiftx,self.world_shifty)
		self.bg_pillar_sprites.draw(self.display_surface) 

		# terrain 
		self.terrain_sprites.update(self.world_shiftx,self.world_shifty)
		self.terrain_sprites.draw(self.display_surface)
		
		# player sprites
		self.playerSpriteGroup.update()
		self.horizontal_movement_collision()
		
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.create_landing_dust()

		# enemy 
		self.enemy_sprites.update(self.world_shiftx,self.world_shifty)
		self.constraint_sprites.update(self.world_shiftx,self.world_shifty)
		self.check_enemy_collisions(self.Player)
		# self.enemyHit(self.Player)
		# self.constraint_sprites.draw(self.display_surface)
		self.enemy_collision_reverse()
		self.enemy_sprites.draw(self.display_surface)
		self.explosion_sprites.update(self.world_shiftx,self.world_shifty)
		self.explosion_sprites.draw(self.display_surface)

		# dust particles 
		self.dust_sprite.update(self.world_shiftx,self.world_shifty)
		self.dust_sprite.draw(self.display_surface)

		self.scroll_x()
		# self.scroll_y()
		self.playerSpriteGroup.draw(self.display_surface)
		self.goal.update(self.world_shiftx,self.world_shifty)
		self.goBack.update(self.world_shiftx,self.world_shifty)
		self.goal.draw(self.display_surface)
		self.goBack.draw(self.display_surface)

		#UI
		self.UI.show_health(self.Player.hp,100)

		#camera
		self.camera.custom_draw(self.Player)
		self.camera.update()

		#check if player attacked enemy
		self.enemyGotHit(self.Player)

		
