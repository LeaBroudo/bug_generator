import regions as loc
import maya.cmds as cmds

class Abdomen:
    def __init__(self, body):
        self.body = body
        self.abdomen = loc.abdomen 
        self.arm_locs = loc.arm_locs["abdomen"]

    ### Full Abdomen ###
    def tiltAbdomen(self, deg):
        #get min x of thorax
        #move pivot there
        #select thorax and abdomen, set soft select 
        #tilt degrees 

    def scaleAbdomen(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
    
    ### Patterns ###
    def pattern(self, vars):
        #iterate through faces and lift up varying degrees?

    def vertRidges(self, num):

    def horizRidges(self, num):

    ### Front ###
    def scaleFront(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def moveFront(self, move_x, move_y, move_z):
        #set soft select 
        #move
    
    ### Mid ###
    def scaleMid(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def moveMid(self, move_x, move_y, move_z):
        #set soft select 
        #move
    
    ### Back ###
    def scaleBack(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 

    def moveback(self, move_x, move_y, move_z):
        #set soft select 
        #move

    def endTaper(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
    
    ### Face ###
    def scaleFace(self, scale_x, scale_y, scale_z):
        #turn symmetry off from self.body
        #set soft select 
        #scale
        #turn symmetry on 
    
    def moveFace(self, move_x, move_y, move_z):
        #set soft select 
        #move