import maya.cmds as cmds
import maya.mel as mel
import os
import random
import regions as loc
import arm_control
import wing_control

#import head_control
#import arm_control
#import thorax_control
#import wing_control
#import abdomen_control

### General Body ###
class Body:
    def __init__(self):

        # User Variables
        self.name = "" 
        self.arms = []
        self.wings = []

    def importAll(self, name, wing_num, abd_arm_num, thorax_arm_num):
        self.name = name
        
        # Import body
        pathVar = os.path.dirname(__file__) # This stores the current working directory
        cmds.file( pathVar+"./Body.mb", i=True )
        #cmds.rename( "polySurface1", self.name )

        #Import Thorax to copy
        if abd_arm_num != 0 or thorax_arm_num != 0:
            
            #import arm
            temp_arm = "temp_arm"
            cmds.file( pathVar+"/Arm.mb", i=True, dns=True )
            cmds.rename( "Arm_", temp_arm )

            #Create separate arm locs
            positions = random.sample(loc.thorax_arms, abd_arm_num)
            positions.extend(random.sample(loc.abdomen_arms, thorax_arm_num))

            for pos in positions:
                #Duplicate, add to list
                idx = str(len(self.arms)+1)
                arm_name = "Arm_"+idx
                cmds.duplicate(temp_arm, name=arm_name, rc=True, rr=True)
                self.arms.append(arm_control.Arm(idx))
                #Parent Body
                cmds.parent(arm_name, "BODY")
                #Bind Skin
                cmds.skinCluster(loc.arm+idx, loc.arm_mesh+idx)
                #Copy Skin Weights 
                mel.eval("select -r "+loc.arm_mesh)
                mel.eval("select -add "+loc.arm_mesh+idx)
                mel.eval("copySkinWeights  -noMirror -surfaceAssociation closestPoint -influenceAssociation closestJoint;")
                #move to correct location
                cmds.move(pos[0], pos[1], pos[2], loc.arm+idx)
                #Add lattice
                #cmds.select(arm_name)
                #cmds.lattice( dv=(6, 10, 25), oc=True, n="arm"+idx )
                #cmds.rename("arm"+idx+"Lattice","arm_latt_"+idx)
                #cmds.delete("arm"+idx+"Base")
                #cmds.parent("arm_latt_"+idx, arm_name)
                #Duplicate to other side
                temp_right = arm_name+"_R"
                cmds.duplicate(arm_name, name=temp_right,ic=True, rc=False) 
                cmds.scale(1,1,-1, temp_right)
                cmds.move(loc.right_diff, temp_right, z=True)
                cmds.rename(temp_right+"|"+loc.arm_mesh+idx, loc.arm_mesh+idx+"_R")
                #cmds.parent(loc.arm_mesh+idx+"_R", arm_name)
                cmds.delete(temp_right+"|"+loc.arm+idx)
                #Parent joint to body
                cmds.parent(loc.arm+idx, loc.body_arm_joints[pos[0]])

            #DELETE original
            cmds.delete(temp_arm)

        #Import Wings to copy
        if wing_num != 0:

            #import wing
            temp_wing = "temp_wing"
            cmds.file( pathVar+"/Wing.mb", i=True, dns=True )
            cmds.rename( "Wing_", temp_wing )
            
            #Find Positions
            positions = random.sample(loc.wing_locs, wing_num)
            
            for pos in positions:
                #Duplicate, add to list
                idx = str(len(self.wings)+1)
                wing_name = "Wing_"+idx
                cmds.duplicate(temp_wing, name=wing_name, rc=True)
                self.wings.append(wing_control.Wing(wing_name))
                #move to correct location
                cmds.move(pos[0], pos[1], pos[2], wing_name)
                cmds.rotate(loc.wing_rot[0],loc.wing_rot[1],loc.wing_rot[2], wing_name)
                #Parent Body
                cmds.parent(wing_name, "BODY")
                #Add lattice
                cmds.select(wing_name)
                cmds.lattice( dv=(20, 4, 20), oc=True, n="wing"+idx )
                cmds.rename("wing"+idx+"Lattice","wing_latt_"+idx)
                cmds.delete("wing"+idx+"Base")
                cmds.parent("wing_latt_"+idx, wing_name)
                #Duplicate to other side
                cmds.duplicate(wing_name, name=wing_name+"_R", ic=True, rc=True) 
                cmds.delete("wing_latt_"+str(int(idx)+1))
                cmds.scale(1,1,-1, wing_name+"_R")
                cmds.rotate(-1*loc.wing_rot[0],-1*loc.wing_rot[1],loc.wing_rot[2], wing_name+"_R")
                cmds.move(-3.25, wing_name+"_R", z=True)

            #DELETE original
            cmds.delete(temp_wing)


        return self.arms, self.wings

    
    #Deformers 



#######
#Start attaching lattice manip to methods
#Finish rest of UI

