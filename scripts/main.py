import maya.cmds as cmds
import os
import regions as loc
#import head_control
#import arm_control
#import thorax_control
#import wing_control
#import abdomen_control

### General Body ###
class Body:
    def __init__(self, name, wing_num, abd_arm_num, thorax_arm_num):
        
        # User Variables
        self.name = name
        self.wing_num = wing_num 
        self.a_arms = []
        self.t_arms = []

        # Set Variables
        self.wing_locs = loc.wing_locs
        self.arm_locs = loc.arm_locs


        # Import body
        pathVar = os.path.dirname(__file__) # This stores the current working directory
        cmds.file( pathVar+"/Body.mb", i=True )
        cmds.rename( "polySurface1", self.name )

        # Set Symmetry 
        cmds.select(self.name)
        cmds.symmetricModelling(about="object", axis="Z")

        #Import Thorax/Wings to copy
        if abd_arm_num != 0 or thorax_arm_num != 0:
            #IMPORT ARM

            self.createAbdomenArms(abd_arm_num)
            self.createThoraxArms(thorax_arm_num)

            #DELETE original

        # Iterate through user preferences and instantiate global vars w/ body objects?

    def createAbdomenArms(self, num):
        if num == 0: return 
        
        #Choose random locations for each arm
        #Create new arm object
        #Duplicate, add to list, move to correct location
    
    def createThoraxArms(self, num):
        if num == 0: return 
        
        #Choose random locations for each arm
        #Create new arm object
        #Duplicate, add to list, move to correct location

    #Deformers 

