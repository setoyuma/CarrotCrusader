#!/usr/bin/Python3
#from pygame_functions import *
import pygame as pg, sys, os, csv
from debug import debug
from pygame.locals import *
from settings import *

pg.init() # initiates pg
pg.display.set_caption('CC alpha-v0.1.1')
pg.display.set_icon(gameIcon)
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

animation_database['idle'] = load_animation('./assets/Player/idle',[6,6,0,6,6,0,6,6])
animation_database['run'] = load_animation('./assets/Player/run',[0,5,5,5,0,5,5,5])
animation_database['jump'] = load_animation('./assets/Player/jump',[1,1,1])
animation_database['wallJump'] = load_animation('./assets/Player/walljump',[1,1,1])
# animation_database['attack'] = load_animation('../assets/Player/attack',[1,1,1])

'''SET DEFAULT PLAYER ANIM STATE'''
player_action = 'idle'
player_frame = 0
player_flip = False

'''PLAYER RECT'''
player_rect = pg.Rect(200,1270,32,32)


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


'''MAP INSTANCE'''
game_map = load_map('./map/CarrotCrusaderStage0MapWIP.csv')

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
            match tile:
                case'0':
                    DISPLAY.blit(GAMETILES['BreakableBlock'],(x*16-scroll[0],y*16-scroll[1]))
                case'1':
                    DISPLAY.blit(GAMETILES['GrassBlock'],(x*16-scroll[0],y*16-scroll[1]))
                case'2':
                    DISPLAY.blit(GAMETILES['CastleHallBrickFloor'],(x*16-scroll[0],y*16-scroll[1]))
                case'3':
                    DISPLAY.blit(GAMETILES['CastleHallFloorPillar'],(x*16-scroll[0],y*16-scroll[1]))
                case'4':
                    DISPLAY.blit(GAMETILES['BrickBlock'],(x*16-scroll[0],y*16-scroll[1]))
                case'5':
                    DISPLAY.blit(GAMETILES['CastleHallFloorSupport'],(x*16-scroll[0],y*16-scroll[1]))
                case'6':
                    DISPLAY.blit(GAMETILES['ChapelFloor'],(x*16-scroll[0],y*16-scroll[1]))
                case'7':
                    DISPLAY.blit(GAMETILES['ChapelSupport'],(x*16-scroll[0],y*16-scroll[1]))
                case'8':
                    DISPLAY.blit(GAMETILES['IceFloor'],(x*16-scroll[0],y*16-scroll[1]))
                case'9':
                    DISPLAY.blit(GAMETILES['IceyBlock'],(x*16-scroll[0],y*16-scroll[1]))
                case'10':
                    DISPLAY.blit(GAMETILES['DrakeGround'],(x*16-scroll[0],y*16-scroll[1]))
                case'11':
                    DISPLAY.blit(GAMETILES['MagmaPoolBlock'],(x*16-scroll[0],y*16-scroll[1]))
                case'12':
                    DISPLAY.blit(GAMETILES['WonderBlockFloor'],(x*16-scroll[0],y*16-scroll[1]))
                case'13':
                    DISPLAY.blit(GAMETILES['WonderBlockSupport'],(x*16-scroll[0],y*16-scroll[1]))
                case'14':
                    DISPLAY.blit(GAMETILES['PillarBlock'],(x*16-scroll[0],y*16-scroll[1]))
                case'15':
                    DISPLAY.blit(GAMETILES['PillarSupport'],(x*16-scroll[0],y*16-scroll[1]))
                case'16':
                    DISPLAY.blit(GAMETILES['GhostTrainFloor'],(x*16-scroll[0],y*16-scroll[1]))
                case'17':
                    DISPLAY.blit(GAMETILES['HauntedPrisonFloor'],(x*16-scroll[0],y*16-scroll[1]))
                case'18':
                    DISPLAY.blit(GAMETILES['HauntedPrisonSupport'],(x*16-scroll[0],y*16-scroll[1]))
                case'19':
                    DISPLAY.blit(GAMETILES['MasterChamberFloor'],(x*16-scroll[0],y*16-scroll[1]))
                case'20':
                    DISPLAY.blit(GAMETILES['MasterChamberSigil'],(x*16-scroll[0],y*16-scroll[1]))
                case'21':
                    DISPLAY.blit(GAMETILES['MasterChamberPillarTop'],(x*16-scroll[0],y*16-scroll[1]))
                case'22':
                    DISPLAY.blit(GAMETILES['MasterChamberPillar'],(x*16-scroll[0],y*16-scroll[1]))
                case'23':
                    DISPLAY.blit(GAMETILES['ClassicBlock'],(x*16-scroll[0],y*16-scroll[1]))
                case'24':
                    DISPLAY.blit(GAMETILES['PlayerSpawn'],(x*16-scroll[0],y*16-scroll[1]))
                    pass
                case'25':
                    DISPLAY.blit(GAMETILES['LevelEnd'],(x*16-scroll[0],y*16-scroll[1]))
                    pass
                case ('-1','24','25'):
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

    '''RESPAWN'''
    if player_rect.y > tile_rects.pop()[1]+200:
        print('RESPAWN\n')
        player_rect.x = 200
        player_rect.y = 1270


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

    '''FALL SPRITE SETUP'''
    if collisions['bottom']:
        air_timer = 0
        vertical_momentum = 1
    if not collisions['bottom']:
        air_timer += 2
        player_action,player_frame = change_action(player_action,player_frame,'jump') 
    
    '''WALL HUG SPRITE SETUP'''
    if not collisions['bottom']:
        if collisions ['left'] and jumping:
            player_action,player_frame = change_action(player_action,player_frame,'wallJump') 
    if not collisions['bottom']:
        if collisions ['right'] and jumping:
            player_action,player_frame = change_action(player_action,player_frame,'wallJump') 

    '''HEAD BUMP'''
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
                if air_timer < 3:
                    jumping = True
                    vertical_momentum = -4.5
                #wall jump
                if collisions['right'] and jumping:
                    vertical_momentum = -5
                    jumping = False
                if collisions['left'] and jumping:
                    vertical_momentum = -5
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
