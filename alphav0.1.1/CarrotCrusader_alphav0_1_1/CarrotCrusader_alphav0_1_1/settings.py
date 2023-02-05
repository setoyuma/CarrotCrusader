import pygame as pg
gameIcon = pg.image.load('./imgs/tiles/gameIcon.png')
# WINDOW_SIZE = (1000,700)
WINDOW_SIZE = (1080,720)
CAPTION = pg.display.set_caption('Carrot Crusader')
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
DISPLAY = pg.Surface((300,200)) # used as the surface for rendering, which is scaled
TRUESCROLL = [0,0]
jumping = False
DEVMODE = False
'''TILE DICTIONARY'''
GAMETILES = {
    'BreakableBlock' : pg.image.load('./imgs/tiles/BreakableBlock.png'),
    'GrassBlock' : pg.image.load('./imgs/tiles/GrassBlock.png'),
    'ClassicBlock' : pg.image.load('./imgs/tiles/Classic.png'),
    'IceFloor' : pg.image.load('./imgs/tiles/IceFloor.png'),
    'IceyBlock' : pg.image.load('./imgs/tiles/IceyBlock.png'),
    'PillarBlock' : pg.image.load('./imgs/tiles/PillarBlock.png'),
    'PillarSupport' : pg.image.load('./imgs/tiles/PillarSupportBlock.png'),
    'ChapelSupport' : pg.image.load('./imgs/tiles/ChapelSupport.png'),
    'ChapelFloor' : pg.image.load('./imgs/tiles/ChapelFloor.png'),
    'CastleHallFloorSupport' : pg.image.load('./imgs/tiles/CastleHallFloorSupportBlock.png'),
    'CastleHallBrickFloor' : pg.image.load('./imgs/tiles/CastleHallBrickFloorBlock.png'),
    'BrickBlock' : pg.image.load('./imgs/tiles/BrickBlock.png'),
    'HauntedPrisonFloor' : pg.image.load('./imgs/tiles/Haunted Prison Floor.png'),
    'GhostTrainFloor' : pg.image.load('./imgs/tiles/Ghost Train Floor.png'),
    'MagmaPoolBlock' : pg.image.load('./imgs/tiles/Magma Pool Block.png'),
    'MasterChamberFloor' : pg.image.load('./imgs/tiles/Master Chamber Floor.png'),
    'MasterChamberPillarTop' : pg.image.load('./imgs/tiles/Master Chamber Sigil Pillar Top.png'),
    'MasterChamberPillar' : pg.image.load('./imgs/tiles/Master Chamber Sigil Pillar.png'),
    'MasterChamberSigil' : pg.image.load('./imgs/tiles/Master Chamber Sigil Support.png'),
    'DrakeGround' : pg.image.load('./imgs/tiles/Drake Ground Floor.png'),
    'WonderBlockFloor' : pg.image.load('./imgs/tiles/Wonder Block Floor.png'),
    'WonderBlockSupport' : pg.image.load('./imgs/tiles/Wonder Block Support.png'),
    'CastleHallFloorPillar' : pg.image.load('./imgs/tiles/Castle Hall Floor Pillar.png'),
    'HauntedPrisonSupport' : pg.image.load('./imgs/tiles/Haunted Prison Support.png'),
    'PlayerSpawn' : pg.image.load('./imgs/tiles/AgravaineSpawnIcon.png'),
    'LevelEnd' : pg.image.load('./imgs/tiles/LevelEndMarker.png'),
}
