import pygame as pg, sys, os
from pygame.locals import *
from settingsR import *
from player import *

class Game:

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption('game')
        self.screen = pg.display.set_mode(WINDOWSIZE,0,32)

        self.scaleDisplay = scaleDisplay 

        self.clock = pg.time.Clock()

        self.gameMap = self.loadMap('map2')

        self.background_objects = [
            [0.25,[120,10,70,400]],
            [0.25,[280,30,40,400]],
            [0.5,[30,40,40,400]],
            [0.5,[130,90,100,400]],
            [0.5,[300,80,120,400]]
            ]


        self.player = Player()
    
    def loadMap(self,path) -> list:
        f = open(path + '.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map


    def run(self):
        while True: # game loop
            
            self.player.moveCheck()
            self.player.animate(self.scaleDisplay)


            self.scaleDisplay.fill((146,244,255)) # clear screen by filling it with blue

            #parallax bg stuff
            true_scroll[0] += (self.player.player_rect.x-true_scroll[0]-152)/20
            true_scroll[1] += (self.player.player_rect.y-true_scroll[1]-106)/20
            scroll[0] = int(scroll[0])
            scroll[1] = int(scroll[1])
            #draw background items with parallax effect
            pg.draw.rect(self.scaleDisplay,(7,80,75),pg.Rect(0,120,300,80))
            for background_object in self.background_objects:
                obj_rect = pg.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
                if background_object[0] == 0.5:
                    pg.draw.rect(self.scaleDisplay,(14,222,150),obj_rect)
                else:
                    pg.draw.rect(self.scaleDisplay,(9,91,85),obj_rect)


            #world tiles
            y = 0
            #draw tiles based on map data
            for layer in self.gameMap:
                x = 0
                for tile in layer:
                    if tile == '1':
                        self.scaleDisplay.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
                    if tile == '2':
                        self.scaleDisplay.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
                    if tile != '0':
                        tileRects.append(pg.Rect(x*16,y*16,16,16))
                    x += 1
                y += 1

            for event in pg.event.get(): # event loop
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.player.moving_right = True
                    if event.key == K_LEFT:
                        self.player.moving_left = True
                    if event.key == K_UP:
                        if self.player.air_timer < 6:
                            self.player.vertical_momentum = -5
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        self.player.moving_right = False
                    if event.key == K_LEFT:
                        self.player.moving_left = False
        
            self.screen.blit(pg.transform.scale(scaleDisplay,WINDOWSIZE),(0,0))
            pg.display.update()
            self.clock.tick(60)



if __name__ == '__main__':
    game = Game()
    game.run()