import maya.cmds as cmds
import os
import regions as loc

### General Body ###
class Body:
    def __init__(self, name, wing_bool, arm_dict):
        
        # User Variables
        self.name = name
        self.wing_bool = wing_bool 
        self.arm_dict = arm_dict #arm_dict = {"head": 1, "thorax":2, "abdomen":3}

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

        # Iterate through user preferences and instantiate global vars w/ body objects?

