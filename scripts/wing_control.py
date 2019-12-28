import regions as loc
import maya.cmds as cmds

class Wing:
    def __init__(self, body):
        self.body = body
        

    ### Full Abdomen ###
    def tiltWings(self, deg):
        #get min x of thorax
        #move pivot there
        #select thorax and abdomen, set soft select 
        #tilt degrees 

    def scaleWings(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
    
    ### Patterns ###
    def pattern(self, vars):
        #iterate through faces and lift up varying degrees?

    ### Scale Regions ###
    def scaleOut(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def scaleIn(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def scaleBase(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
    
    