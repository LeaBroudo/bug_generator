import regions as loc
import maya.cmds as cmds

class Arm:
    def __init__(self, arm_num):
    
        self.arm = loc.arm + str(arm_num)
        self.shoulder = loc.shoulder + str(arm_num)
        self.femur = loc.femur + str(arm_num)
        self.knee = loc.knee + str(arm_num)
        self.tibia = loc.tibia + str(arm_num)
        self.tarsus = loc.tarsus + str(arm_num)
        self.hand = loc.hand + str(arm_num)

        self.tarsus_len = 1
        self.tarsus_rad = 1
        
        self.tibia_len = 1
        self.tibia_rad = 1

        self.femur_len = 1
        self.femur_rad = 1

        self.shoulder_len = 1
        self.shoulder_rad = 1
        
        
    ### Full Arm ###
    def tiltArm(self, deg):
        #get min x of thorax
        #move pivot there
        #select thorax and abdomen, set soft select 
        #tilt degrees 
        """
        TODO
        """

    def scaleArm(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        """
        TODO
        """

    ### Shoulder ###
    def lenShoulder(self, num):
        cmds.move(0,0,(-1*self.shoulder_len)+num, self.shoulder, r=True)
        self.shoulder_len = num

    def radShoulder(self, num):
        cmds.scale(1,num/self.shoulder_rad,num/self.shoulder_rad, self.shoulder, r=True)
        self.shoulder_rad = num
    
    ### Femur ###
    def lenFemur(self, num):
        cmds.move(0,0,(-1*self.femur_len)+num, self.femur, r=True)
        self.femur_len = num

    def radFemur(self, num):
        cmds.scale(1,num/self.femur_rad,num/self.femur_rad, self.femur, r=True)
        self.femur_rad = num

    def tiltKnee(self, deg):
        """
        TODO
        """
    
    ### Tibia ###
    def lenTibia(self, num):
        cmds.move(0,0,(-1*self.tibia_len)+num, self.tibia, r=True)
        self.tibia_len = num

    def radTibia(self, num):
        cmds.scale(1,num/self.tibia_rad,num/self.tibia_rad, self.tibia, r=True)
        self.tibia_rad = num
    
    ### Tarsus ###
    def lenTarsus(self, num):
        cmds.move(0,0,(-1*self.tarsus_len)+num, self.tarsus, r=True)
        self.tarsus_len = num

    def radTarsus(self, num):
        cmds.scale(1,num/self.tarsus_rad,num/self.tarsus_rad, self.tarsus, r=True)
        self.tarsus_rad = num
    