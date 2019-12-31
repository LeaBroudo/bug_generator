import maya.cmds as cmds
import os
import random
import regions as loc
import arm_control

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



        # Import body
        pathVar = os.path.dirname(__file__) # This stores the current working directory
        cmds.file( pathVar+"./Body.mb", i=True )
        #cmds.rename( "polySurface1", self.name )

        # Set Symmetry 
        #cmds.select(self.name)
        #cmds.symmetricModelling(about="object", axis="Z")

        #Import Thorax/Wings to copy
        if abd_arm_num != 0 or thorax_arm_num != 0:
            
            #import arm
            temp_arm = "temp_arm"
            cmds.file( pathVar+"/Arm.mb", i=True )
            cmds.rename( "Arm_Arm", temp_arm )

            #Create separate arm locs
            positions = random.sample(loc.thorax_arms, abd_arm_num)
            positions.extend(random.sample(loc.abdomen_arms, thorax_arm_num))

            for pos in positions:
                #Duplicate, add to list
                idx = str(len(self.a_arms)+1)
                arm_name = "Arm_"+idx
                cmds.duplicate(temp_arm, name=arm_name, rc=True)
                self.a_arms.append(arm_control.Arm(arm_name))
                #move to correct location
                cmds.move(pos[0], pos[1], pos[2], arm_name)
                #Parent Body
                cmds.parent(arm_name, "BODY")
                #Add lattice
                cmds.select(arm_name)
                cmds.lattice( dv=(6, 10, 25), oc=True, n="arm"+idx )
                cmds.rename("arm"+idx+"Lattice","arm_latt_"+idx)
                cmds.delete("arm"+idx+"Base")
                cmds.parent("arm_latt_"+idx, arm_name)
                #Duplicate to other side
                cmds.duplicate(arm_name, name=arm_name+"_R", ic=True, rc=True) #THEN MOVE
                cmds.delete("arm_latt_"+str(int(idx)+1))
                cmds.scale(1,1,-1, arm_name+"_R")
                cmds.move(-3.25, arm_name+"_R", z=True)



        
            #DELETE original
            cmds.delete(temp_arm)

        # Iterate through user preferences and instantiate global vars w/ body objects?

    
    #Deformers 



#######
#Add leg and wing locations 
#Be able to use Create with legs/wings
#Start attaching lattice manip to methods
#Finish rest of UI

