import regions as loc
import maya.cmds as cmds

class Head:
    def __init__(self):
        #self.name = name
        self.antLen = 1
        self.antWidth = 1
        self.manLen = 1
        self.manWidth = 1
        self.manHeight = 1

    ### Helpers ###
    def getPortion(self, latt, start, end, add=False):
        selectStr = latt + ".pt"
        for i in range(3):
            selectStr += "[" + str(start[i]) + ":" + str(end[i]) + "]"
        
        if add == True:
            cmds.select(selectStr, add=True)
        else:
            cmds.select(selectStr)
    
    
    ### Full Head ###
    def tiltHead(self, deg):
        #get max x of head

        #move pivot there

        #set soft select 
        #tilt head degrees 
        '''
        TODO
        '''

    def scaleHead(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        '''
        TODO
        '''

    ### Neck ###
    def scaleNeckBase(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on
        '''
        TODO
        '''

    def scaleNeck(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        '''
        TODO
        '''
    
    def moveNeck(self, move_x, move_y, move_z):
        #set soft select 
        #move
        '''
        TODO
        '''
    
    ### Face ###
    def scaleFace(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        '''
        TODO
        '''
    
    def moveFace(self, move_x, move_y, move_z):
        #set soft select 
        #move
        '''
        TODO
        '''

    def pattern(self, vars):
        #iterate through faces and lift up varying degrees?
        '''
        TODO
        '''

    ### Nose ###
    def scaleNose(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        '''
        TODO
        '''
    
    def moveNose(self, move_x, move_y, move_z):
        #set soft select 
        #move
        '''
        TODO
        '''

    ### Eyes ###
    def sizeEyes(self, num):
        front_mid = [1,2,4]
        self.getPortion(loc.man_str, loc.man_latt[0], front_mid)
        cmds.scale(1.0/self.manLen, 1, 1, r=True)
        cmds.scale(num, 1, 1, r=True)
        self.manLen = num

    def distEyes(self, num):
        front_mid = [1,2,4]
        self.getPortion(loc.man_str, loc.man_latt[0], front_mid)
        cmds.scale(1.0/self.manLen, 1, 1, r=True)
        cmds.scale(num, 1, 1, r=True)
        self.manLen = num

    ### Mandibles ###
    def lenMandibles(self, num):
        front_mid = [1,2,4]
        self.getPortion(loc.man_str, loc.man_latt[0], front_mid)
        cmds.scale(1.0/self.manLen, 1, 1, r=True)
        cmds.scale(num, 1, 1, r=True)
        self.manLen = num

    def widthMandibles(self, num):
        front_mid = [1,2,4]
        self.getPortion(loc.man_str, loc.man_latt[0], front_mid)
        cmds.scale(1, 1, 1.0/self.manWidth, r=True)
        cmds.scale(1, 1, num, r=True)
        self.manWidth = num

    def heightMandibles(self, num):
        front_mid = [1,2,4]
        self.getPortion(loc.man_str, loc.man_latt[0], front_mid)
        cmds.scale(1, 1.0/self.manHeight, 1, r=True)
        cmds.scale(1, num, 1, r=True)
        self.manHeight = num
        

    ### Antennas ###
    
    #Lengthen
    def lengthAntenna(self, num):
       front_mid = [1,2,2]
       self.getPortion(loc.ant_str, loc.ant_latt[0], front_mid)
       cmds.scale(1.0/self.antLen, 1, 1, r=True)
       cmds.scale(num, 1, 1, r=True)
       self.antLen = num

    #Width
    def widthAntenna(self, num):
       front = [0,2,2]
       self.getPortion(loc.ant_str, loc.ant_latt[0], front)
       cmds.scale(1, 1, 1.0/self.antWidth, r=True)
       cmds.scale(1, 1, num, r=True)
       self.antWidth = num

    #bend deformer
    #length
    #radius
    #tip radius




    