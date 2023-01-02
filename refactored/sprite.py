import pygame as pg


class Sprite:
    def __init__(self) -> None:
        self.animationFrames = {}
        self.animation_database = {}
        self.animation_database['run'] = self.loadAnimation('../imgs/vegnath',[1,1])
        self.animation_database['idle'] = self.loadAnimation('../imgs/vegnath',[1,1,0])

    def loadAnimation(self,path,frame_durations):
        animation_name = path.split('/')[-1]
        animation_frame_data = []
        n = 0
        for frame in frame_durations:
            animation_frame_id = animation_name + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            # player_animations/idle/idle0.png
            animation_image = pg.image.load(img_loc).convert()
            animation_image.set_colorkey((255,255,255))
            self.animationFrames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data
    
    def changeAction(self,action_var,frame,new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var,frame

