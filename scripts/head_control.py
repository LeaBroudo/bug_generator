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

        self.eyeSize = 1
        self.eyeDist = 1

        self.faceLen = 1
        self.faceRad = 1
        self.faceTilt = 1

        self.neck_min = 1
        self.neck_max = 1

    ### Helpers ###
    def getPortion(self, latt, start, end, add=False):
        selectStr = latt + ".pt"
        for i in range(3):
            selectStr += "[" + str(start[i]) + ":" + str(end[i]) + "]"
        
        if add == True:
            cmds.select(selectStr, add=True)
        else:
            cmds.select(selectStr)
    

    ### Neck ###
    def scaleNeck(self, num):
        if num <= 1:
            front_mid = [1,2,2]
            self.getPortion(loc.neck_str, loc.neck_latt[0], front_mid)
            cmds.scale(1, 1.0/self.neck_min, 1.0/self.neck_min, r=True)
            self.neck_min = num

        else:
            mid = [1,0,0]
            back = [2,2,2]
            self.getPortion(loc.neck_str, mid, back)
            cmds.scale(1, 1.0/self.neck_max, 1.0/self.neck_max, r=True)
            self.neck_max = num

        cmds.scale(1, num, num, r=True)
    
    ### Face ###
    def lenFace(self, num):
        front_mid = [2,2,2]
        self.getPortion(loc.face_str, loc.face_latt[0], front_mid)
        cmds.scale(1.0/self.faceLen, 1, 1, r=True)
        cmds.scale(num, 1, 1, r=True)
        self.faceLen = num
    
    def radFace(self, num):
        front_mid = [2,2,2]
        self.getPortion(loc.face_str, loc.face_latt[0], front_mid)
        cmds.scale(1, 1.0/self.faceRad, 1.0/self.faceRad, r=True)
        cmds.scale(1, num, num, r=True)
        self.faceRad = num

    def tiltFace(self, num):
        cmds.rotate(0, 0, (-1*self.faceTilt) + num, loc.face_str)

    ### Eyes ###
    def sizeEyes(self, num):
        cmds.select(loc.eye_l_joint)
        cmds.select(loc.eye_r_joint, add=True)

        cmds.scale(num/self.eyeSize, num/self.eyeSize, num/self.eyeSize, r=True)
        self.eyeSize = num

    def distEyes(self, num):
        self.getPortion(loc.eye_l_str, loc.eye_latt[0], loc.eye_latt[1])
        self.getPortion(loc.eye_r_str, loc.eye_latt[0], loc.eye_latt[1], True)

        cmds.scale(1.0/self.eyeDist, 1.0/self.eyeDist, 1.0/self.eyeDist, r=True)
        cmds.scale(num, num, num, r=True)
        self.eyeDist = num

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




    