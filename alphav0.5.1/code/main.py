import pygame as pg, sys
from settings import * 
from level import Level
from game_data import level_0
from pygame.locals import *
from ui import UI

# pg setup
pg.init()
screen = pg.display.set_mode((screen_width,screen_height))
clock = pg.time.Clock()
level = Level(level_0,screen)
# ui = UI(screen)
health_bar = pg.image.load('../graphics/UI/HealthBar/HealthBar.png').convert_alpha()
BG = pg.image.load('../graphics/decoration/sky/DarkSky.png')


while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			print('\n Game Closed \n')
			pg.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_q:
				print('\n Game Closed \n')
				pg.quit()
				sys.exit()

	
	# ui.show_health(100,100)
	screen.fill('#0f0024')
	screen.blit(BG,(0,0))
	screen.blit(health_bar,(0,0))
	level.run()

	pg.display.update()
	clock.tick(60)