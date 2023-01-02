import pygame as pg

WINDOWSIZE = (600,400)
FPS = 60
TILESIZE = 16
true_scroll = [0,0]
scroll = true_scroll.copy()
tileRects = []
scaleDisplay = pg.Surface((WINDOWSIZE[0]/2, WINDOWSIZE[1]/2))
grass_img = pg.image.load('../imgs/tiles/Classic.png')
dirt_img = pg.image.load('../imgs/tiles/GrassBlock.png')