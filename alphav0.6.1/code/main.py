import pygame as pg, sys
from settings import * 
from level import Level
from game_data import level_0
from pygame.locals import KEYDOWN

# pg setup
pg.init()
screen = pg.display.set_mode((screen_width,screen_height))
clock = pg.time.Clock()
level = Level(level_0,screen)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			print('\nGame Closed\n')
			pg.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == pg.K_q:
				print('\nGame Closed\n')
				pg.quit()
				sys.exit()

	
	screen.fill('grey')
	level.run()

	pg.display.update()
	clock.tick(60)