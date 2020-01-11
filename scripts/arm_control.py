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

        self.spread_dist = [0,0,0,0]
        self.knee_height = 0
        
        
    ### Full Arm ###
    def spread(self, num):
        cmds.move(0,0,(num*self.shoulder_len)-self.spread_dist[0], self.shoulder, r=True, os=True, wd=True)
        cmds.move(0,0,(num*self.femur_len)-self.spread_dist[1], self.femur, r=True, os=True, wd=True)
        cmds.move(0,0,(num*self.tibia_len)-self.spread_dist[2], self.tibia, r=True, os=True, wd=True)
        cmds.move(0,0,(num*self.tarsus_len)-self.spread_dist[3], self.tarsus, r=True, os=True, wd=True)

        self.spread_dist = [num*self.shoulder_len, num*self.femur_len, num*self.tibia_len, num*self.tarsus_len]

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

    ### Knee ###
    def heightKnee(self, num):
        cmds.move(0,(-1*self.knee_height)+num,0, self.femur, r=True)
        cmds.move(0,(self.knee_height)-num,0, self.tibia, r=True)
        self.knee_height = num
    
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
    