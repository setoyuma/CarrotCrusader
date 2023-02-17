import pygame as pg, sys
from settings import * 
from level import Level
from game_data import levels
from pygame.locals import *
from ui import UI

# pg setup
pg.init()
screen = pg.display.set_mode((screen_width,screen_height))
clock = pg.time.Clock()
currentLevel = 1
level = Level(levels[currentLevel],screen)
ui = UI(screen)
health_bar = pg.image.load('../graphics/UI/HealthBar/HealthBar.png').convert_alpha()
BG = pg.image.load('../graphics/decoration/sky/DarkSky.png')
font = pg.font.Font('../graphics/UI/ARCADEPI.ttf',30)

while True:
	if level.Player.hp == 0:
			# loseBar = font.render('You Lose',True,'yellow','black')
			# screen.blit(loseBar,(screen_width/2,screen_height/2),level.Player.rect)
			print('\n You Lose \n')
			# pg.quit()
			# sys.exit()

	'''CHANGE TO NEXT LEVEL'''
	if pg.sprite.spritecollide(level.goal.sprite, level.playerSpriteGroup,False):
		# print('Touched Goal')
		print('amount of levels:',len(levels))
		print('current level',currentLevel)
		if currentLevel < len(levels) :
			currentLevel += 1
			level = Level(levels[currentLevel],screen)
			print('current level',currentLevel)
		if currentLevel == len(levels):
			print('game complete')
			currentLevel - 1
			print('current level',currentLevel)
	
	'''CHANGE TO PREVIOUS LEVEL'''
	if pg.sprite.spritecollide(level.goBack.sprite, level.playerSpriteGroup,False):
		print('Touched Go Back')
		currentLevel -= 1
		if currentLevel < 1:
			print('game at Start')
			currentLevel = 1
			print('current level',currentLevel)
		else:
			level = Level(levels[currentLevel],screen)
			print('current level',currentLevel)
		if currentLevel > 1:
			level.wentBack = True
			level = Level(levels[currentLevel],screen)
			print('current level',currentLevel)
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

		

	screen.fill('#0f0024')
	screen.blit(BG,(0,0))
	# screen.blit(health_bar,(0,0))
	level.run()

	pg.display.update()
	clock.tick(60)