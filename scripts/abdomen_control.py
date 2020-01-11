import regions as loc
import maya.cmds as cmds

class Abdomen:
    def __init__(self):

        self.abd_1_dist = 1
        self.abd_2_dist = 1
        self.abd_3_dist = 1

        self.abd_1_scale = 1
        self.abd_2_scale = 1
        self.abd_3_scale = 1

    ### Full Abdomen ###
    def tiltAbdomen(self, deg):
        '''
        TODO
        '''

    def lenAbdomen(self, num):
        front_move, mid_move, back_move = num/3.0, num/3.0, num/3.0
        
        cmds.move((-self.abd_1_dist)+front_move,0,0,loc.abd_front, r=True)
        cmds.move((-self.abd_2_dist)+mid_move,0,0,loc.abd_mid, r=True)
        cmds.move((-self.abd_3_dist)+back_move,0,0,loc.abd_back, r=True)

        self.abd_1_dist = front_move
        self.abd_2_dist = mid_move
        self.abd_3_dist = back_move
    
    ### Patterns ###
    def pattern(self, vars):
        #iterate through faces and lift up varying degrees?
        '''
        TODO
        '''

    def vertRidges(self, num):
        '''
        TODO
        '''

    def horizRidges(self, num):
        '''
        TODO
        '''

    ### Front ###
    def scaleFront(self, num):
        cmds.select(loc.abd_front)
        cmds.scale(1,num/self.abd_1_scale, num/self.abd_1_scale, r=True)
        self.abd_1_scale = num

    ### Mid ###
    def scaleMid(self, num):
        cmds.select(loc.abd_mid)
        cmds.scale(1,num/self.abd_2_scale, num/self.abd_2_scale, r=True)
        self.abd_2_scale = num
    
    ### Back ###
    def scaleBack(self, num):
        cmds.select(loc.abd_back)
        cmds.scale(1,num/self.abd_3_scale, num/self.abd_3_scale, r=True)
        self.abd_3_scale = num 


