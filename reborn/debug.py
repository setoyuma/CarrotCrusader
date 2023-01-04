import pygame as pg
pg.init()
font = pg.font.Font(None,30)

def debug(info,y=10,x=10):
    displaySurface = pg.display.get_surface()
    debugSurface = font.render(str(info),True,'White')
    debugRect = debugSurface.get_rect(topleft=(x,y))
    pg.draw.rect(displaySurface,'Black',debugRect)
    displaySurface.blit(debugSurface,debugRect)
 