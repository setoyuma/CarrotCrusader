import pygame as pg
pg.init()
font = pg.font.Font(None,30)

def debug(surf,info,y=10,x=10):
    displaySurface = pg.display.get_surface()
    debugSurface = font.render(str(info),True,'Red')
    debugRect = debugSurface.get_rect(topleft=(x,y))
    pg.draw.rect(displaySurface,'Grey',debugRect)
    displaySurface.blit(debugSurface,debugRect)
 