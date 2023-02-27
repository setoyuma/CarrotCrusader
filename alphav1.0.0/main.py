import pygame as pg, sys
from settings import * 
from level import Level
from pygame.locals import KEYDOWN

def main():
    # pg setup
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pg.display.set_caption('Platformer')
    clock = pg.time.Clock()

    level = Level()

    while True:
        # event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_r:
                    main()
                    
        
        screen.fill(BG_COLOR)
        level.run()
        
        font = pg.font.Font(None,30)
        fpsCounter = str(int(clock.get_fps()))
        text = font.render(f"FPS: {fpsCounter}",True,'white','black')
        textPos = text.get_rect(centerx=1000, y=10)
        screen.blit(text,textPos)

        # drawing logic
        pg.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()