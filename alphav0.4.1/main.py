import pygame as pg,sys,csv,os
from pygame.locals import *
from settings import *
from tileClass import Tile
from levelClass import Level
from ui import UI


class Game():
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(WINDOWSIZE,0,32)
        self.scaleDisplay = DISPLAY
        # self.scaleDisplay = pg.Surface((640,350)) # 2x scaling
        # self.scaleDisplay = pg.Surface((320,175)) # 3x scaling
        self.clock = pg.time.Clock()
        self.BG = pg.image.load('../assets/Sky/DarkSky.png')
        self.BG = pg.transform.scale(self.BG, (WINDOWSIZEHALF))

        '''Map Setup'''
        self.LEVEL = self.loadMap(LEVELMAP)
        # self.map = Level(self.LEVEL,self.screen)
        self.map = Level(self.LEVEL,self.scaleDisplay)

        '''UI SETUP'''
        self.UI = UI(self.scaleDisplay)


    def loadMap(self, path):
        gameMap = []
        with open(os.path.join(path)) as data:
            data = csv.reader(data,delimiter=",")
            for row in data:
                gameMap.append(list(row))
        # print(gameMap)
        return gameMap

    def Run(self):
        while True:
            # self.screen.fill('black')
            # self.scaleDisplay.fill('black')
            self.scaleDisplay.blit(self.BG,(0,0))
            self.map.Run()
            self.UI.show_health(100,100)
            
            #event handler
            for event in pg.event.get():
                if event.type == QUIT:
                        print("\nGame Closed\n")
                        pg.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        print("\nGame Closed\n")
                        pg.quit()
                        sys.exit()

            self.screen.blit(pg.transform.scale(self.scaleDisplay,WINDOWSIZE),(0,0))    #scale the display up 
            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.Run()