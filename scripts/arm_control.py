import regions as loc
import maya.cmds as cmds

class Arm:
    def __init__(self, arm_name):
        """
        TODO
        """

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
    def lenTibia(self, len):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        """
        TODO
        """

    def radTibia(self, rad):
        #set soft select 
        #move
        """
        TODO
        """
    
    ### Tarsus ###
    def lenTarsus(self, len):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
        """
        TODO
        """

    def radTarsus(self, rad):
        #set soft select 
        #move
        """
        TODO
        """
    