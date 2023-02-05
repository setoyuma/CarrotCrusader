import pygame as pg
from settings02 import *
from os import walk

def importFolder(path):
    surfaceList = []
    
    for _,__,imgFiles in walk(path):
        for img in imgFiles:
            fullPath = path + '/' + img
            imgSurface = pg.image.load(fullPath).convert_alpha()
            surfaceList.append(imgSurface)

    return surfaceList