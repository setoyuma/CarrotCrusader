import pygame as pg
WINDOW_SIZE = (1920,1080)
CAPTION = pg.display.set_caption('Carrot Crusader')
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
DISPLAY = pg.Surface((300,200)) # used as the surface for rendering, which is scaled
TRUESCROLL = [0,0]
