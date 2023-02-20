import pygame as pg
from settings import *

class UI:
	def __init__(self,surface):

		# setup 
		self.display_surface = surface 

		# health 
		self.health_bar = pg.image.load('../graphics/UI/HealthBar/HealthBar.png').convert_alpha()
		self.health_bar_topleft = (0,0)
		self.bar_max_width = 168
		self.bar_height = 24

		# # coins 
		# self.coin = pg.image.load('../graphics/ui/coin.png').convert_alpha()
		# self.coin_rect = self.coin.get_rect(topleft = (50,61))
		# self.font = pg.font.Font('../graphics/ui/ARCADEPI.ttf',30)

	def show_health(self,current,full):
		current_health_ratio = current / full
		current_bar_width = self.bar_max_width * current_health_ratio
		health_bar_rect = pg.Rect((self.health_bar_topleft[0]+74,self.health_bar_topleft[1]+34),(current_bar_width,self.bar_height))
		pg.draw.rect(self.display_surface,'red',health_bar_rect,0,1,-1,80,-1,152)
		self.display_surface.blit(self.health_bar,self.health_bar_topleft)

	# def show_coins(self,amount):
	# 	self.display_surface.blit(self.coin,self.coin_rect)
	# 	coin_amount_surf = self.font.render(str(amount),False,'#33323d')
	# 	coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 4,self.coin_rect.centery))
	# 	self.display_surface.blit(coin_amount_surf,coin_amount_rect)