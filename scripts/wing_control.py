import regions as loc
import maya.cmds as cmds

class Wing:
    def __init__(self, wing_num):
        self.top_len = 0
        self.low_len = 0
        self.wing_scale = 1

        self.wing = loc.wing + str(wing_num)
        self.wing_base = loc.wing_base + str(wing_num)
        self.wing_low = loc.wing_low + str(wing_num)
        self.wing_top = loc.wing_top + str(wing_num)

    def tiltWings(self, deg):
        #get min x of thorax
        #move pivot there
        #select thorax and abdomen, set soft select 
        #tilt degrees 
        '''
        TODO
        '''

    def scaleWings(self, num):
        cmds.scale(num/self.wing_scale,1,num/self.wing_scale, self.wing_base, r=True)
        self.wing_scale = num

    def scaleTop(self, num):
        cmds.move(0,0,(-1*self.top_len)+num, self.wing_top, r=True, os=True, wd=True)
        self.top_len = num

    def scaleLow(self, num):
        cmds.move(0,0,(-1*self.low_len)+num, self.wing_low, r=True, os=True, wd=True)
        self.low_len = num

    
    