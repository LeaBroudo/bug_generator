import regions as loc
import maya.cmds as cmds

class Head:
    def __init__(self, body):
        self.head = loc.head 
        self.body = body

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
    def scaleEyes(self, scale_x, scale_y, scale_z):
        #select eyes 
        #set soft select 
        #scale 
        '''
        TODO
        '''

    ### Mandibles ###
    def scaleMandibles(self, scale_x, scale_y, scale_z):
        #select eyes 
        #set soft select 
        #scale 
        '''
        TODO
        '''


    ### Antennas ###
    #bend deformer
    #length
    #radius
    #tip radius