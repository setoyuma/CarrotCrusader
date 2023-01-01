import pygame as pg, sys
from settings import *
from mapData import *
from debug import debug
from levelClass import Level

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT)) # main display surface
        self.win = pg.Surface((500,400))   #surface used for image scaling onto main display surface ^
        self.clock = pg.time.Clock()
        pg.display.set_caption("Red4")

        self.level = Level(self.win)
        

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print("\nGame closed\n")
                    pg.quit()
                    sys.exit()
                
                self.screen.fill('black')
                self.scaled_win = pg.transform.scale(self.win, self.screen.get_size()) #scale images
                self.screen.blit(self.scaled_win,(0,0)) #blit scaled images to main display surface
                self.level.run()
                pg.display.flip()
                self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()