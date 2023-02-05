import pygame as pg
gameIcon = pg.image.load('../assets/tiles/gameIcon.png')
# WINDOW_SIZE = (1000,700)
WINDOWSIZE = (1080,720)
CAPTION = pg.display.set_caption('Carrot Crusader')
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(WINDOWSIZE,0,32) # initiate the window
DISPLAY = pg.Surface((300,200)) # used as the surface for rendering, which is scaled
TILESIZE = 16
FPS = 60
LEVELMAP = './TestMap1.csv'
TRUESCROLL = [0,0]
jumping = False
DEVMODE = False
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
    'GhostTrainFloor' : pg.image.load('../assets/tiles/Ghost Train Floor.png'),
    'HauntedPrisonFloor' : pg.image.load('../assets/tiles/Haunted Prison Floor.png'),
    'HauntedPrisonSupport' : pg.image.load('../assets/tiles/Haunted Prison Support.png'),
    'MasterChamberFloor' : pg.image.load('../assets/tiles/Master Chamber Floor.png'),
    'MasterChamberPillarTop' : pg.image.load('../assets/tiles/Master Chamber Sigil Pillar Top.png'),
    'MasterChamberPillar' : pg.image.load('../assets/tiles/Master Chamber Sigil Pillar.png'),
    'MasterChamberSigil' : pg.image.load('../assets/tiles/Master Chamber Sigil Support.png'),
    'DrakeGround' : pg.image.load('../assets/tiles/Drake Ground Floor.png'),
    'MagmaPoolBlock' : pg.image.load('../assets/tiles/Magma Pool Block.png'),
    'PillarBlock' : pg.image.load('../assets/tiles/PillarBlock.png'),
    'PillarSupport' : pg.image.load('../assets/tiles/PillarSupportBlock.png'),
    'WonderBlockFloor' : pg.image.load('../assets/tiles/Wonder Block Floor.png'),
    'WonderBlockSupport' : pg.image.load('../assets/tiles/Wonder Block Support.png'),
    'CastleHallFloorPillar' : pg.image.load('../assets/tiles/Castle Hall Floor Pillar.png'),
    'PlayerSpawn' : pg.image.load('../assets/tiles/AgravaineSpawnIcon.png'),
    'LevelEnd' : pg.image.load('../assets/tiles/LevelEndMarker.png'),
}
