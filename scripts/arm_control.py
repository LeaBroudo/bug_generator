import regions as loc
import maya.cmds as cmds

class Arm:
    def __init__(self, arm_num):
    
        self.arm_latt = loc.arm_str + str(arm_num)

        self.tarsus_len = 1
        self.tibia_len = 1
        
        
        #self.tib_tars_dist = self.tibs_tars_Dist()
        self.tib_tars_dist = 0

    ### Helpers ###
    def getPortion(self, latt, start, end, add=False):
        selectStr = latt + ".pt"
        for i in range(3):
            selectStr += "[" + str(start[i]) + ":" + str(end[i]) + "]"
        
        if add == True:
            cmds.select(selectStr, add=True)
        else:
            cmds.select(selectStr)

    def tibs_tars_Dist(self):
        tarsus_start = ".pt[0][0][21]"
        tibia_start =  ".pt[0][0][16]"
        
        pA = cmds.xform(self.arm_latt + tarsus_start, q=True, t=True, ws=True)
        pB = cmds.xform(self.arm_latt + tibia_start, q=True, t=True, ws=True)
        
        print("tibs-tars dist: " + str(pA[2]-pB[2]))

        return pA[2]-pB[2]
    


    
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

    ### Femur ###
    def lenFemur(self, len):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        """
        TODO
        """

    def radFemur(self, rad):
        #set soft select 
        #move
        """
        TODO
        """

    def tiltKnee(self, deg):
        """
        TODO
        """
    
    ### Tibia ###
    def lenTibia(self, num):
        self.getPortion(self.arm_latt, loc.tibia_latt[0], loc.tibia_latt[1])
        cmds.scale(1, 1, 1.0/self.tibia_len, r=True)
        cmds.scale(1, 1, num, r=True)
        self.tibia_len = num

        # Move tarsus back
        diff = self.tibs_tars_Dist() - self.tib_tars_dist
        print("difference: "+str(diff))
        self.getPortion(self.arm_latt, loc.tarsus_latt[0], loc.tarsus_latt[1])
        cmds.move(1, 1, -1*diff, r=True)

    def radTibia(self, rad):
        #set soft select 
        #move
        """
        TODO
        """
    
    ### Tarsus ###
    def lenTarsus(self, num):
        self.getPortion(self.arm_latt, loc.tarsus_latt[0], loc.tarsus_latt[1])
        cmds.scale(1, 1, 1.0/self.tarsus_len, r=True)
        cmds.scale(1, 1, num, r=True)
        self.tarsus_len = num

        #Update Distance
        self.tib_tars_dist = self.tibs_tars_Dist()


    def radTarsus(self, rad):
        #set soft select 
        #move
        """
        TODO
        """
    