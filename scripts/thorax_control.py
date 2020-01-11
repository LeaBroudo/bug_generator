import regions as loc
import maya.cmds as cmds

class Thorax:
    def __init__(self):

        self.thx_2_dist = 1
        self.thx_3_dist = 1

        self.thx_1_scale = 1
        self.thx_2_scale = 1
        self.thx_3_scale = 1

    ### Full Thorax ###
    def tiltThorax(self, deg):
        #get min x of thorax
        #move pivot there
        #select thorax and abdomen, set soft select 
        #tilt degrees 
        '''
        TODO
        '''

    def lenThorax(self, num):
        mid_move = num/3.0
        back_move = (2.0*num)/3.0
        
        cmds.move((-self.thx_2_dist)+mid_move,0,0,loc.thx_mid, r=True)
        cmds.move((-self.thx_3_dist)+back_move,0,0,loc.thx_back, r=True)

        self.thx_2_dist = mid_move
        self.thx_3_dist = back_move

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
        cmds.select(loc.thx_front)
        cmds.scale(1,num/self.thx_1_scale, num/self.thx_1_scale, r=True)
        self.thx_1_scale = num
    
    ### Mid ###
    def scaleMid(self, num):
        cmds.select(loc.thx_mid)
        cmds.scale(1,num/self.thx_2_scale, num/self.thx_2_scale, r=True)
        self.thx_2_scale = num
    
    ### Back ###
    def scaleBack(self, num):
        cmds.select(loc.thx_back)
        cmds.scale(1,num/self.thx_3_scale, num/self.thx_3_scale, r=True)
        self.thx_3_scale = num 

    
    