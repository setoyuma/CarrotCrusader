import pygame as pg, sys

class Camera(pg.sprite.Group):
	def __init__(self):
		super().__init__()
		self.displaySurface = pg.display.get_surface()

		#camera offset
		self.offset = pg.math.Vector2()
		self.half_w = self.displaySurface.get_size()[0] // 2
		self.half_h = self.displaySurface.get_size()[1] // 2

		# box setup
		self.camera_borders = {'left': 100, 'right': 100, 'top': 100, 'bottom': 100}
		l = self.camera_borders['left']
		t = self.camera_borders['top']
		w = self.displaySurface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
		h = self.displaySurface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
		self.camera_rect = pg.Rect(l,t,w,h)

		# camera speed
		self.keyboard_speed = 5
		self.mouse_speed = 0.2


		# zoom 
		self.zoom_scale = 1
		self.internal_surf_size = (2500,2500)
		self.internal_surf = pg.Surface(self.internal_surf_size, pg.SRCALPHA)
		self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
		self.internal_surface_size_vector = pg.math.Vector2(self.internal_surf_size)
		self.internal_offset = pg.math.Vector2()
		self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
		self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

	def box_target_camera(self,target):

		if target.rect.left < self.camera_rect.left:
			self.camera_rect.left = target.rect.left

		if target.rect.right > self.camera_rect.right:
			self.camera_rect.right = target.rect.right

		if target.rect.top < self.camera_rect.top:
			self.camera_rect.top = target.rect.top
			
		if target.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = target.rect.bottom

	def custom_draw(self,player):
		self.box_target_camera(player)
		

		# active elements
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
			self.internal_surf.blit(sprite.image,offset_pos)

		scaled_surf = pg.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
		scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))

		self.displaySurface.blit(scaled_surf,scaled_rect)



		pg.draw.rect(self.displaySurface,'yellow',self.camera_rect,5) #show camera box