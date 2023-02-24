import pygame, sys
from random import randint

class Camera(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()

		# camera offset 
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surface.get_size()[0] // 2
		self.half_h = self.display_surface.get_size()[1] // 2

		# box setup
		self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
		l = self.camera_borders['left']
		t = self.camera_borders['top']
		w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
		h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
		self.camera_rect = pygame.Rect(l,t,w,h)

		# camera speed
		self.keyboard_speed = 5
		self.mouse_speed = 0.2

		# zoom 
		self.zoom_scale = 1
		self.internal_surf_size = (2500,2500)
		self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
		self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
		self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
		self.internal_offset = pygame.math.Vector2()
		self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
		self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

	def center_target_camera(self,target):
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y = target.rect.centery - self.half_h

	def box_target_camera(self,target):

		if target.rect.left < self.camera_rect.left:
			self.camera_rect.left = target.rect.left
		if target.rect.right > self.camera_rect.right:
			self.camera_rect.right = target.rect.right
		if target.rect.top < self.camera_rect.top:
			self.camera_rect.top = target.rect.top
		if target.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = target.rect.bottom

		self.offset.x = self.camera_rect.left - self.camera_borders['left']
		self.offset.y = self.camera_rect.top - self.camera_borders['top']

	def keyboard_control(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]: self.camera_rect.x -= self.keyboard_speed
		if keys[pygame.K_d]: self.camera_rect.x += self.keyboard_speed
		if keys[pygame.K_w]: self.camera_rect.y -= self.keyboard_speed
		if keys[pygame.K_s]: self.camera_rect.y += self.keyboard_speed

		self.offset.x = self.camera_rect.left - self.camera_borders['left']
		self.offset.y = self.camera_rect.top - self.camera_borders['top']

	def mouse_control(self):
		mouse = pygame.math.Vector2(pygame.mouse.get_pos())
		mouse_offset_vector = pygame.math.Vector2()

		left_border = self.camera_borders['left']
		top_border = self.camera_borders['top']
		right_border = self.display_surface.get_size()[0] - self.camera_borders['right']
		bottom_border = self.display_surface.get_size()[1] - self.camera_borders['bottom']

		if top_border < mouse.y < bottom_border:
			if mouse.x < left_border:
				mouse_offset_vector.x = mouse.x - left_border
				pygame.mouse.set_pos((left_border,mouse.y))
			if mouse.x > right_border:
				mouse_offset_vector.x = mouse.x - right_border
				pygame.mouse.set_pos((right_border,mouse.y))
		elif mouse.y < top_border:
			if mouse.x < left_border:
				mouse_offset_vector = mouse - pygame.math.Vector2(left_border,top_border)
				pygame.mouse.set_pos((left_border,top_border))
			if mouse.x > right_border:
				mouse_offset_vector = mouse - pygame.math.Vector2(right_border,top_border)
				pygame.mouse.set_pos((right_border,top_border))
		elif mouse.y > bottom_border:
			if mouse.x < left_border:
				mouse_offset_vector = mouse - pygame.math.Vector2(left_border,bottom_border)
				pygame.mouse.set_pos((left_border,bottom_border))
			if mouse.x > right_border:
				mouse_offset_vector = mouse - pygame.math.Vector2(right_border,bottom_border)
				pygame.mouse.set_pos((right_border,bottom_border))

		if left_border < mouse.x < right_border:
			if mouse.y < top_border:
				mouse_offset_vector.y = mouse.y - top_border
				pygame.mouse.set_pos((mouse.x,top_border))
			if mouse.y > bottom_border:
				mouse_offset_vector.y = mouse.y - bottom_border
				pygame.mouse.set_pos((mouse.x,bottom_border))

		self.offset += mouse_offset_vector * self.mouse_speed

	def zoom_keyboard_control(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_q]:
			self.zoom_scale += 0.1
		if keys[pygame.K_e]:
			self.zoom_scale -= 0.1

	def custom_draw(self,player):
		
		self.center_target_camera(player)
		# self.box_target_camera(player)
		# self.keyboard_control()
		# self.mouse_control()
		# self.zoom_keyboard_control()

		# active elements
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
			self.internal_surf.blit(sprite.image,offset_pos)

		scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
		scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))

		self.display_surface.blit(scaled_surf,scaled_rect)
