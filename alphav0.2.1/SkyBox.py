# import pygame as pg
# from settings02 import verticalTileNumber, TILESIZE, SCREENWIDTH

# class SkyBox:
#     def __init__(self, horizon):
#         self.top = pg.image.load('../assets/Sky/sky_top.png')
#         self.middle = pg.image.load('../assets/Sky/sky_middle.png')
#         self.bottom = pg.image.load('../assets/Sky/sky_bottom.png')
#         self.horizon = horizon

#         #stretch
#         self.top = pg.transform.scale(self.top,(SCREENWIDTH,TILESIZE))
#         self.middle = pg.transform.scale(self.middle,(SCREENWIDTH,TILESIZE))
#         self.bottom = pg.transform.scale(self.bottom,(SCREENWIDTH,TILESIZE))

#     def draw(self,surf):
#         for row in range(verticalTileNumber):
#             y = row * TILESIZE
#             surf.blit(self.top,(0,y))