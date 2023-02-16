import pygame as pg
gameIcon = pg.image.load('../assets/gameIcon.ico')
# WINDOW_SIZE = (1000,700)
TILESIZE = 16
verticalTileNumber = 11
SCREENHEIGHT = verticalTileNumber * TILESIZE
SCREENWIDTH = 1000
WINDOWSIZE = (1000,800)
# WINDOWSIZE = (1200,1000)
WINDOWSIZEHALF = (600,360)
CAPTION = pg.display.set_caption('Carrot Crusader')
ICON = pg.display.set_icon(pg.image.load('../assets/gameIcon.png'))
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(WINDOWSIZE) # initiate the window
# DISPLAY = pg.Surface((300,200)) # used as the surface for rendering, which is scaled 3x
# DISPLAY = pg.Surface((480,288)) # used as the surface for rendering, which is scaled 2.5x
DISPLAY = pg.Surface((440,362)) # used as the surface for rendering, which is scaled 2.75x
FPS = 60
LEVELMAP = '../assets/map/TestMap.csv'
# LEVELMAP = '../map/WIPMAP.csv'
'''TILE DICTIONARY'''
GAMETILES = {
    'BreakableBlock' : pg.image.load('../assets/tiles/BreakableBlock.png'),
    'GrassBlock' : pg.image.load('../assets/tiles/GrassBlock.png'),
    'ClassicBlock' : pg.image.load('../assets/tiles/Classic.png'),
    'IceFloor' : pg.image.load('../assets/tiles/IceFloor.png'),
    'IceyBlock' : pg.image.load('../assets/tiles/IceyBlock.png'),
    'ChapelSupport' : pg.image.load('../assets/tiles/ChapelSupport.png'),
    'ChapelFloor' : pg.image.load('../assets/tiles/ChapelFloor.png'),
    'CastleHallFloorSupport' : pg.image.load('../assets/tiles/CastleHallFloorSupportBlock.png'),
    'CastleHallBrickFloor' : pg.image.load('../assets/tiles/CastleHallBrickFloorBlock.png'),
    'BrickBlock' : pg.image.load('../assets/tiles/BrickBlock.png'),
    'GhostTrainFloor' : '../assets/tiles/AnimTiles/GhostTrain', #anim block
    'HauntedPrisonFloor' : '../assets/tiles/AnimTiles/HauntedPrison', #anim block
    'HauntedPrisonSupport' : pg.image.load('../assets/tiles/Haunted Prison Support.png'),
    'MasterChamberFloor' : '../assets/tiles/AnimTiles/MasterFloor', #anim block
    'MasterChamberPillarTop' : '../assets/tiles/AnimTiles/MastersPillarTop', #anim block
    'MasterChamberPillar' : '../assets/tiles/AnimTiles/MastersPillar', #anim block
    'MasterChamberSigil' : '../assets/tiles/AnimTiles/MCSigil', #anim block
    'DrakeGround' : '../assets/tiles/AnimTiles/DrakeGround', #anim block
    'MagmaPoolBlock' : '../assets/tiles/AnimTiles/MagmaPool', 
    'PillarBlock' : pg.image.load('../assets/tiles/PillarBlock.png'),
    'PillarSupport' : pg.image.load('../assets/tiles/PillarSupportBlock.png'),
    'WonderBlockFloor' : '../assets/tiles/AnimTiles/WonderBlock/', #anim block
    'WonderBlockSupport' : '../assets/tiles/AnimTiles/WonderBlockSupport', #anim block
    'CastleHallFloorPillar' : pg.image.load('../assets/tiles/Castle Hall Floor Pillar.png'),
    'PlayerSpawn' : pg.image.load('../assets/tiles/AgravaineSpawnIcon.png'),
    'LevelEnd' : pg.image.load('../assets/tiles/LevelEndMarker.png'),
    'WoodFloor' : pg.image.load('../assets/tiles/WoodFloor.png'),
    'TempleOfSixFloor' : pg.image.load('../assets/tiles/TempleOfSixFloor.png'),
    'TempleOfSixFloorSupport' : pg.image.load('../assets/tiles/TempleOfSixFloorSupport.png'),
    'TempleOfSixFloorCracked' : pg.image.load('../assets/tiles/TempleOfSixFloorCracked.png'),
    'TempleOfSixFloorRug' : pg.image.load('../assets/tiles/TempleOfSixFloorRug.png'),
    'DrakeCeiling' : pg.image.load('../assets/tiles/DrakeCeiling.png'),
    'IceyWall' : pg.image.load('../assets/tiles/IceyWall.png'),
    'IceyCorner' : pg.image.load('../assets/tiles/IceyCorner.png'),
    'MagmaSpurt' : pg.image.load('../assets/tiles/MagmaSpurt.png'),
    'ChapelFoundation' : pg.image.load('../assets/tiles/ChapelFoundation.png'),
    'ChapelCorner' : pg.image.load('../assets/tiles/ChapelCorner.png'),
    'ChapelCeiling' : pg.image.load('../assets/tiles/ChapelCeiling.png'),
    'ChapelWall' : pg.image.load('../assets/tiles/ChapelWall.png'),
    'ChapelUnderFloor' : pg.image.load('../assets/tiles/ChapelUnderFloor.png'),
    'EnemyConstraint' : pg.image.load('../assets/tiles/EnemyConstraint.png'),
}
