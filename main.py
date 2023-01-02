import pygame as pg, sys
from settings import *
from mapData import *
from debug import debug
from levelClass import Level
 
from pygame.locals import *

# from playerClass import Player

class Game:
    def __init__(self) -> None:
 
        pg.init()
        self.screen = pg.display.set_mode((WINDOWSIZE)) # main display surface
        # self.win = pg.Surface((500,400))   #surface used for image scaling onto main display surface ^
        self.clock = pg.time.Clock()
        pg.display.set_caption("Red4")

        self.level = Level()
        # self.level = Level(self.screen)
        

    def run(self): 
        while True: #game loop

            self.screen.fill("black")

            #event handler
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        print("\nGame closed\n")
                        pg.quit()
                        sys.exit()
                
                
            # self.win.fill("grey")
            # self.scaled_win = pg.transform.scale(self.win, self.screen.get_size()) #scale images
            # self.screen.blit(self.scaled_win,(0,0)) #blit scaled images to main display surface

            self.level.run()

            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()