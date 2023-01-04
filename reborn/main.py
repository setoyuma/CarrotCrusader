from pygame_functions import *
import pygame as pg, sys, os, csv
from debug import debug
from pygame.locals import *
from settings import *

pg.init() # initiates pg

'''ANIMATION FUNC'''
global animation_frames
animation_frames = {}

def load_animation(path,frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        # player_animations/idle/idle0.png
        animation_image = pg.image.load(img_loc).convert_alpha()
        animation_image.set_colorkey('black')
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame

'''ANIMATION SETUP'''
animation_database = {}

animation_database['idle'] = load_animation('../imgs/Player/idle',[6,6,6,6,6,6,6,6])
animation_database['run'] = load_animation('../imgs/Player/run',[0,5,5,5,5,5,5,5])
animation_database['jump'] = load_animation('../imgs/Player/jump',[1,1,1])
# animation_database['attack'] = load_animation('../imgs/Player/attack',[1,1,1])

'''SET DEFAULT PLAYER ANIM STATE'''
player_action = 'idle'
player_frame = 0
player_flip = False

'''PLAYER RECT'''
player_rect = pg.Rect(100,100,32,32)


'''CREATE BG OBJECTS'''
background_objects = [
    [0.25,[120,10,17,400]],
    [0.25,[250,2,40,400]],
    [0.25,[450,30,90,400]],
    [1,[340,3,70,400]],
    [0.25,[530,80,14,400]],
    [0.5,[30,40,40,400]],
    [0.5,[130,90,100,400]],
    [0.5,[300,80,120,400]],
    ]


'''PLAYER COLLISIONS TEST FUNC'''
def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

'''PLAYER MOVE FUNC'''
def move(rect,movement,tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

'''LOAD MAP'''
def load_map(path):
    game_map = []
    with open(os.path.join(path)) as data:
        data = csv.reader(data,delimiter=",")
        for row in data:
            game_map.append(list(row))
    return game_map

'''MAP INSTANCE'''
game_map = load_map('../imgs/Tiled/TestMap1.csv')

'''TILE DICTIONARY'''
GAME_TILES = {
    'ClassicBlock' : pg.image.load('../imgs/tiles/Classic.png'),
    'GrassBlock' : pg.image.load('../imgs/tiles/GrassBlock.png'),
    'IceFloor' : pg.image.load('../imgs/tiles/IceFloor.png'),
    'IceyBlock' : pg.image.load('../imgs/tiles/IceyBlock.png'),
    'PillarBlock' : pg.image.load('../imgs/tiles/PillarBlock.png'),
    'PillarSupport' : pg.image.load('../imgs/tiles/PillarSupportBlock.png'),
    'ChapelSupport' : pg.image.load('../imgs/tiles/ChapelSupport.png'),
    'ChapelFloor' : pg.image.load('../imgs/tiles/ChapelFloor.png'),
    'CastleHallFloorSupport' : pg.image.load('../imgs/tiles/CastleHallFloorSupportBlock.png'),
    'CastleHallBrickFloor' : pg.image.load('../imgs/tiles/CastleHallBrickFloorBlock.png'),
    'BrickBlock' : pg.image.load('../imgs/tiles/BrickBlock.png'),
    'BreakableBlock' : pg.image.load('../imgs/tiles/BreakableBlock.png'),
    'HauntedPrisonFloor' : pg.image.load('../imgs/tiles/Haunted Prison Floor.png'),
    'GhostTrainFloor' : pg.image.load('../imgs/tiles/Ghost Train Floor.png'),
    'MagmaPoolBlock' : pg.image.load('../imgs/tiles/Magma Pool Block.png'),
    'MasterChamberFloor' : pg.image.load('../imgs/tiles/Master Chamber Floor.png'),
    'MasterChamberPillarTop' : pg.image.load('../imgs/tiles/Master Chamber Sigil Pillar Top.png'),
    'MasterChamberPillar' : pg.image.load('../imgs/tiles/Master Chamber Sigil Pillar.png'),
    'MasterChamberSupport' : pg.image.load('../imgs/tiles/Master Chamber Sigil Support.png'),
    'DrakeGround' : pg.image.load('../imgs/tiles/Drake Ground Floor.png'),
    'WonderBlockFloor' : pg.image.load('../imgs/tiles/Wonder Block Floor.png'),
    'WonderBlockSupport' : pg.image.load('../imgs/tiles/Wonder Block Support.png'),
    'CastleHallFloorPillar' : pg.image.load('../imgs/tiles/Castle Hall Floor Pillar.png'),
    'HauntedPrisonSupport' : pg.image.load('../imgs/tiles/Haunted Prison Support.png'),
}


'''PLAYER STATUS VARS'''
moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0


'''GAME LOOP'''
while True: # game loop
    # if DEVMODE:
    #     print('Developer Mode:',DEVMODE)
    # print(vertical_momentum)
    DISPLAY.fill((0,0,0)) #main bg color

    TRUESCROLL[0] += (player_rect.x-TRUESCROLL[0]-152)/20
    TRUESCROLL[1] += (player_rect.y-TRUESCROLL[1]-106)/20
    scroll = TRUESCROLL.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])


    '''DRAW BACKGROUND OBJECTS'''
    pg.draw.rect(DISPLAY,(177,80,75),pg.Rect(0,120,300,80)) #halfscreen bg obj
    for background_object in background_objects:
        obj_rect = pg.Rect(
            background_object[1][0]-scroll[0]*background_object[0],
            background_object[1][1]-scroll[1]*background_object[0],
            background_object[1][2],
            background_object[1][3],
            )
        if background_object[0] == 0.5:
            pg.draw.rect(DISPLAY,(143,22,10),obj_rect) #closer bg obj
        else:
            pg.draw.rect(DISPLAY,(129,91,85),obj_rect) #farthest bg obj


    '''DRAW MAP'''
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '0':
                DISPLAY.blit(GAME_TILES['BreakableBlock'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '1':
                DISPLAY.blit(GAME_TILES['CastleHallBrickFloor'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                DISPLAY.blit(GAME_TILES['ClassicBlock'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '3':
                DISPLAY.blit(GAME_TILES['ChapelFloor'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '4':
                DISPLAY.blit(GAME_TILES['IceyBlock'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '5':
                DISPLAY.blit(GAME_TILES['PillarSupport'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '6':
                DISPLAY.blit(GAME_TILES['DrakeGround'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '7':
                DISPLAY.blit(GAME_TILES['HauntedPrisonFloor'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '8':
                DISPLAY.blit(GAME_TILES['BrickBlock'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '9':
                DISPLAY.blit(GAME_TILES['CastleHallFloorSupport'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '10':
                DISPLAY.blit(GAME_TILES['ChapelSupport'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '11':
                DISPLAY.blit(GAME_TILES['GrassBlock'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '12':
                DISPLAY.blit(GAME_TILES['IceFloor'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '13':
                DISPLAY.blit(GAME_TILES['PillarBlock'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '14':
                DISPLAY.blit(GAME_TILES['GhostTrainFloor'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '15':
                DISPLAY.blit(GAME_TILES['MagmaPoolBlock'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '16':
                DISPLAY.blit(GAME_TILES['MasterChamberFloor'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '17':
                DISPLAY.blit(GAME_TILES['MasterChamberPillarTop'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '18':
                DISPLAY.blit(GAME_TILES['MasterChamberPillar'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '19':
                DISPLAY.blit(GAME_TILES['MasterChamberSupport'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '20':
                DISPLAY.blit(GAME_TILES['WonderBlockFloor'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '21':
                DISPLAY.blit(GAME_TILES['WonderBlockSupport'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '22':
                DISPLAY.blit(GAME_TILES['CastleHallFloorPillar'],(x*16-scroll[0],y*16-scroll[1]))
            if tile == '23':
                DISPLAY.blit(GAME_TILES['HauntedPrisonSupport'],(x*16-scroll[0],y*16-scroll[1]))
            if tile != '-1':
                tile_rects.append(pg.Rect(x*16,y*16,16,16))
            x += 1
        y += 1


    '''PLAYER MOVEMENT HANDLING'''
    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] += 2
    if moving_left == True:
        player_movement[0] -= 2
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2

    #DEVELOPER MOMENTUM BYPASS
    if DEVMODE:
        if vertical_momentum > 10:
            vertical_momentum = 10
    
    #DEFAULT MOMENTUM RULES
    elif vertical_momentum > 3:
        vertical_momentum = 3

    if player_movement[0] == 0:
        player_action,player_frame = change_action(player_action,player_frame,'idle')
    if player_movement[0] > 0:
        player_flip = False
        player_action,player_frame = change_action(player_action,player_frame,'run')
    if player_movement[0] < 0:
        player_flip = True
        player_action,player_frame = change_action(player_action,player_frame,'run')

    player_rect,collisions = move(player_rect,player_movement,tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 1
    if not collisions['bottom']:
        air_timer += 1
        player_action,player_frame = change_action(player_action,player_frame,'jump') 
    if vertical_momentum > 1:
        if collisions['top']:
            vertical_momentum = 0
            air_timer = 0

    '''PLAY ANIMATION'''
    player_frame += 1
    if player_frame >= len(animation_database[player_action]):
        player_frame = 0
    player_img_id = animation_database[player_action][player_frame]
    player_img = animation_frames[player_img_id]
    DISPLAY.blit(pg.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))

    '''EVENT HANDLER'''
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                print("\nGame Closed\n")
                pg.QUIT
                sys.exit()
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
            if event.key == K_SPACE:
                if air_timer < 4:
                    jumping = True
                    vertical_momentum = -3.5
                #wall jump
                if jumping and collisions['right']:
                    vertical_momentum = -4.5
                    jumping = False
                if jumping and collisions['left']:
                    vertical_momentum = -4.5
                    jumping = False
            
            #dev mode
            if event.key == K_HOME:
                DEVMODE = True
                print('DEVELOPER MODE:',DEVMODE)
            if event.key == K_END:
                DEVMODE = False
                print('DEVELOPER MODE:',DEVMODE)
            
            if DEVMODE and event.key == K_RSHIFT:
                print('RSHIFT')
                vertical_momentum = -10
            if DEVMODE and event.key == K_SLASH:
                print('hello dev')


        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False
            # if event.key == K_SPACE:
            #     jumping = False
        
    SCREEN.blit(pg.transform.scale(DISPLAY,WINDOW_SIZE),(0,0))
    pg.display.update()
    CLOCK.tick(60)