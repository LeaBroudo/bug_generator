import regions as loc
import maya.cmds as cmds

class Arm:
    def __init__(self, body):
        self.body = body
        

    ### Full Arm ###
    def tiltArm(self, deg):
        #get min x of thorax
        #move pivot there
        #select thorax and abdomen, set soft select 
        #tilt degrees 

    def scaleArm(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    ### Femur ###
    def lenFemur(self, len):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def radFemur(self, rad):
        #set soft select 
        #move

    def tiltKnee(self, deg):
    
    ### Tibia ###
    def lenTibia(self, len):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def radTibia(self, rad):
        #set soft select 
        #move
    
    ### Tarsus ###
    def lenTarsus(self, len):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def radTarsus(self, rad):
        #set soft select 
        #move
    