import pygame as pg
from settings import *
from os import walk
from csv import reader

def importFolder(path):
    surfaceList = []
    
    for _,__,imgFiles in walk(path):
        for img in imgFiles:
            fullPath = path + '/' + img
            imgSurface = pg.image.load(fullPath).convert_alpha()
            surfaceList.append(imgSurface)

    return surfaceList

def import_csv_layout(path):
	terrain_map = []
	with open(path) as map:
		level = reader(map,delimiter = ',')
		for row in level:
			terrain_map.append(list(row))
		return terrain_map