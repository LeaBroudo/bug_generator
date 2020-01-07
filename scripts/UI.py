import maya.cmds as cmds
import pydoc
import random
import main 
import head_control
import arm_control
import regions as loc
from functools import partial

body = main.Body()
head = head_control.Head()
arms = []
wings = []

name = ""
w_num = 0
a_arms = 0
t_arms = 0

window = cmds.window( title="Bug Generator", iconName="Bug Generator", widthHeight=(412, 600) )
cmds.columnLayout( adjustableColumn=True )

# Name
cmds.rowColumnLayout( nc=2, cw=[(1,40),(2,100)], p=window )
cmds.text("Name: ", en=True)
cmds.textField( "bug_name", en=True, tx="Bug") #must connect this to some variable

# Arms/Wings
cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[(1,300),(2, 100)],p=window)

cmds.intSliderGrp( "thoraxArms", l="Thorax Arms: ", v=2, cw3=[100,30,100], min=0, max=3, fmx=3, f=True) 
cmds.checkBox( "thorax_rand", value=False )
cmds.intSliderGrp( "abdomenArms", l="Abdomen Arms: ", v=2, cw3=[100,30,100], min=0, max=3, fmx=3, f=True) 
cmds.checkBox( "abdomen_rand", value=False )

cmds.intSliderGrp( "wings", l="Wings: ", v=2, cw3=[100,30,100], min=0, max=2, fmx=2, f=True) 
cmds.checkBox( "wing_rand", value=False )

# Form body 
def generateBody(*args):
    
    #Name
    global name
    name = str(cmds.textField( "bug_name", q=True, tx=True ))
    
    global w_num, a_arms, t_arms
    #Thorax Arm num
    if cmds.checkBox( "thorax_rand", q=True, v=True ) == True:
        t_arms = random.randint(0,3)
    else:
        t_arms = cmds.intSliderGrp( "thoraxArms", q=True, v=True )

    #Abdomen Arm num
    if cmds.checkBox( "abdomen_rand", q=True, v=True ) == True:
        a_arms = random.randint(0,3)
    else:
        a_arms = cmds.intSliderGrp( "abdomenArms", q=True, v=True )
    
    #Wing num
    if cmds.checkBox( "wing_rand", q=True, v=True ) == True:
        w_num = random.randint(0,2)
    else:
        w_num = cmds.intSliderGrp( "wings", q=True, v=True )
    
    #Create body
    global body
    global arms
    global wings
    arms, wings = body.importAll(name, w_num, a_arms, t_arms)

    
cmds.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 412)],p=window)
cmds.button( label='Generate Body', command=generateBody )

#FOR LOOP FOR ALL BUTTONS



### HEAD ###
### Antenna ###
#length
def lenAnt(*args):
    scaleVal = cmds.floatSliderGrp( "ant_len", q=True, v=True )
    head.lengthAntenna(scaleVal)

cmds.floatSliderGrp( "ant_len", l="Antenna Len: ", v=1, cw3=[100,30,100], min=loc.ant_len[0], max=loc.ant_len[1], fmx=loc.ant_len[1], f=True, dc=lenAnt)

#width
def widthAnt(*args):
    scaleVal = cmds.floatSliderGrp( "ant_width", q=True, v=True )
    head.widthAntenna(scaleVal)

cmds.floatSliderGrp( "ant_width", l="Antenna Width: ", v=1, cw3=[100,30,100], min=loc.ant_width[0], max=loc.ant_width[1], fmx=loc.ant_width[1], f=True, dc=widthAnt)

### Mandibles ###
#Width
def widthMan(*args):
    scaleVal = cmds.floatSliderGrp( "man_width", q=True, v=True )
    head.widthMandibles(scaleVal)

cmds.floatSliderGrp( "man_width", l="Mandible Width: ", v=1, cw3=[100,30,100], min=loc.man_width[0], max=loc.man_width[1], fmx=loc.man_width[1], f=True, dc=widthMan)

#Length
def lenMan(*args):
    scaleVal = cmds.floatSliderGrp( "man_len", q=True, v=True )
    head.lenMandibles(scaleVal)

cmds.floatSliderGrp( "man_len", l="Mandible Length: ", v=1, cw3=[100,30,100], min=loc.man_len[0], max=loc.man_len[1], fmx=loc.man_len[1], f=True, dc=lenMan)

#Height
def heightMan(*args):
    scaleVal = cmds.floatSliderGrp( "man_height", q=True, v=True )
    head.heightMandibles(scaleVal)

cmds.floatSliderGrp( "man_height", l="Mandible Height: ", v=1, cw3=[100,30,100], min=loc.man_height[0], max=loc.man_height[1], fmx=loc.man_height[1], f=True, dc=heightMan)

### Eyes ###
#Size
def sizeEyes(*args):
    scaleVal = cmds.floatSliderGrp( "eye_size", q=True, v=True )
    head.sizeEyes(scaleVal)

cmds.floatSliderGrp( "eye_size", l="Eye Size: ", v=1, cw3=[100,30,100], min=loc.eye_scale[0], max=loc.eye_scale[1], fmx=loc.eye_scale[1], f=True, dc=sizeEyes)

### Face ###
#Length
def lenFace(*args):
    scaleVal = cmds.floatSliderGrp( "face_len", q=True, v=True )
    head.lenFace(scaleVal)

cmds.floatSliderGrp( "face_len", l="Face Length: ", v=1, cw3=[100,30,100], min=loc.face_len[0], max=loc.face_len[1], fmx=loc.face_len[1], f=True, dc=lenFace)

#Radius
def radFace(*args):
    scaleVal = cmds.floatSliderGrp( "face_rad", q=True, v=True )
    head.radFace(scaleVal)

cmds.floatSliderGrp( "face_rad", l="Face Radius: ", v=1, cw3=[100,30,100], min=loc.face_rad[0], max=loc.face_rad[1], fmx=loc.face_rad[1], f=True, dc=radFace)

#Tilt
def tiltFace(*args):
    scaleVal = cmds.floatSliderGrp( "face_tilt", q=True, v=True )
    head.tiltFace(scaleVal)

cmds.floatSliderGrp( "face_tilt", l="Face Tilt: ", v=1, cw3=[100,30,100], min=loc.face_tilt[0], max=loc.face_tilt[1], fmx=loc.face_tilt[1], f=True, dc=tiltFace)

### Neck ###
#Scale
def scaleNeck(*args):
    scaleVal = cmds.floatSliderGrp( "neck_scale", q=True, v=True )
    head.scaleNeck(scaleVal)

cmds.floatSliderGrp( "neck_scale", l="Neck Scale: ", v=1, cw3=[100,30,100], min=loc.neck_scale[0], max=loc.neck_scale[1], fmx=loc.neck_scale[1], f=True, dc=scaleNeck)

### ARM ###
### Tarsus ###
i = 0

def lenTarsus(*args):
    scaleVal = cmds.floatSliderGrp( "len_tarsus", q=True, v=True )
    arms[i].lenTarsus(scaleVal)

cmds.floatSliderGrp( "len_tarsus", l="Tarsus Length: ", v=1, cw3=[100,30,100], min=loc.tarsus_len[0], max=loc.tarsus_len[1], fmx=loc.tarsus_len[1], f=True, dc=lenTarsus)

def lenTibia(*args):
    scaleVal = cmds.floatSliderGrp( "len_tibia", q=True, v=True )
    arms[i].lenTibia(scaleVal)

cmds.floatSliderGrp( "len_tibia", l="Tibia Length: ", v=1, cw3=[100,30,100], min=loc.tibia_len[0], max=loc.tibia_len[1], fmx=loc.tibia_len[1], f=True, dc=lenTibia)




cmds.showWindow( window )