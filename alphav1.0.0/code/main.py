import pygame as pg, sys
from settings import * 
from level import Level
from game_data import level_1
from pygame.locals import KEYDOWN

# pg setup
def main():
	pg.init()
	screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	pg.display.set_caption("CarrotCrusader")
	pg.display.set_icon(pg.image.load("../graphics/gameIcon.ico"))
	clock = pg.time.Clock()
	level = Level(level_1)
	BG = pg.image.load('../graphics/decoration/sky/DarkSky.png')


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
				if event.key == pg.K_r:
					print('\nGame Restarting...\n')
					main()

		

		screen.fill('#0f0024')
		screen.blit(BG,(0,0))
		level.run()

		clock.tick(65)
		font = pg.font.Font(None,30)
		fpsCounter = str(int(clock.get_fps()))
		text = font.render(f"FPS: {fpsCounter}",True,'white','black')
		textPos = text.get_rect(centerx=1000, y=10)
		screen.blit(text,textPos)
		# print(int(clock.get_fps()))

		pg.display.update()

		
if __name__ == '__main__':
	main()