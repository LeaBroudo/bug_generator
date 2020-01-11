import maya.cmds as cmds
import pydoc
import random
import main 
import head_control
import arm_control
import thorax_control
import abdomen_control
import regions as loc
from functools import partial

body = main.Body()
head = head_control.Head()
thx = thorax_control.Thorax()
abd = abdomen_control.Abdomen()
arms = []
wings = []
features = []

name = ""
w_num = 0
a_arms = 0
t_arms = 0

height = 10

window = cmds.window( title="Bug Generator", iconName="Bug Generator", widthHeight=(430, 600) )
scrollLayout = cmds.scrollLayout(verticalScrollBarThickness=16)

# Name
cmds.rowColumnLayout( nc=2, cw=[(1,40),(2,100)], p=window )
cmds.text("Name: ", en=True)
cmds.textField( "bug_name", en=True, tx="Bug") #must connect this to some variable

# Arms/Wings
cmds.rowColumnLayout( numberOfColumns=1, columnWidth=[(1,300)],p=window)

cmds.intSliderGrp( "thoraxArms", l="Thorax Arms: ", v=2, cw3=[100,30,100], min=0, max=3, fmx=3, f=True) 
#cmds.checkBox( "thorax_rand", value=False )
cmds.intSliderGrp( "abdomenArms", l="Abdomen Arms: ", v=2, cw3=[100,30,100], min=0, max=3, fmx=3, f=True) 
#cmds.checkBox( "abdomen_rand", value=False )

cmds.intSliderGrp( "wings", l="Wings: ", v=2, cw3=[100,30,100], min=0, max=2, fmx=2, f=True) 
#cmds.checkBox( "wing_rand", value=False )

#Colors
def bodyColor(*args):
    col = cmds.colorSliderGrp( "col_body", q=True, rgb=True)
    cmds.setAttr( loc.bodyMat+'.color', col[0], col[1], col[2])
cmds.colorSliderGrp( "col_body", l="Body Color: ", rgb=(0.430,0.230,0.11), cw3=[100,30,100], dc=bodyColor)
features.append(("col_body", loc.color_range, bodyColor))

def armColor(*args):
    col = cmds.colorSliderGrp( "col_arm", q=True, rgb=True)
    cmds.setAttr( loc.armMat+'.color', col[0], col[1], col[2])
cmds.colorSliderGrp( "col_arm", l="Arm Color: ", rgb=(0.430,0.230,0.11), cw3=[100,30,100], dc=armColor)
features.append(("col_arm", loc.color_range, armColor))

def wingColor(*args):
    col = cmds.colorSliderGrp( "col_wing", q=True, rgb=True)
    cmds.setAttr( loc.wingMat+'.color', col[0], col[1], col[2])
cmds.colorSliderGrp( "col_wing", l="Wing Color: ", rgb=(0.430,0.230,0.11), cw3=[100,30,100], dc=wingColor)
features.append(("col_wing", loc.color_range, wingColor))

# Form body 
def generateBody(randBool,*args):
    
    #Name
    global name
    name = str(cmds.textField( "bug_name", q=True, tx=True ))
    
    global w_num, a_arms, t_arms
    if randBool == False:
        #Thorax Arm num
        t_arms = cmds.intSliderGrp( "thoraxArms", q=True, v=True )
        #Abdomen Arm num
        a_arms = cmds.intSliderGrp( "abdomenArms", q=True, v=True )   
        #Wing num
        w_num = cmds.intSliderGrp( "wings", q=True, v=True )
    else:
        # Random Body
        w_num = random.randint(0,len(loc.wing_locs))
        t_arms = random.randint(1,len(loc.thorax_arms))
        a_arms = random.randint(1,len(loc.abdomen_arms))
        #Thorax Arm num
        cmds.intSliderGrp( "thoraxArms", e=True, v=t_arms )
        #Abdomen Arm num
        cmds.intSliderGrp( "abdomenArms", e=True, v=a_arms )   
        #Wing num
        cmds.intSliderGrp( "wings", e=True, v=w_num )
    
    #Create body
    global body
    global arms
    global wings
    arms, wings = body.importAll(name, w_num, a_arms, t_arms)
    
    wing_col = cmds.colorSliderGrp( "col_wing", q=True, rgb=True)
    arm_col = cmds.colorSliderGrp( "col_arm", q=True, rgb=True)
    body_col = cmds.colorSliderGrp( "col_body", q=True, rgb=True)
    body.addMaterial(wing_col, arm_col, body_col)

    cmds.intSliderGrp( "curr_Arm", max=len(arms), e=True)
    cmds.intSliderGrp( "curr_Arm", min=0 if len(arms)==0 else 1, e=True)

    cmds.intSliderGrp( "curr_wing", max=len(wings), e=True)
    cmds.intSliderGrp( "curr_wing", min=0 if len(wings)==0 else 1, e=True)


    
cmds.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 412)],p=window)
cmds.button( label='Generate Body', command=partial(generateBody, False) )
cmds.separator( h=height,st="none" )


### HEAD ###
### Antenna ###
#length
def lenAnt(*args):
    scaleVal = cmds.floatSliderGrp( "ant_len", q=True, v=True )
    head.lengthAntenna(scaleVal)

cmds.floatSliderGrp( "ant_len", l="Antenna Len: ", v=1, cw3=[100,30,100], min=loc.ant_len[0], max=loc.ant_len[1], fmx=loc.ant_len[1], f=True, dc=lenAnt)
features.append(("ant_len", loc.ant_len, lenAnt))

#width
def widthAnt(*args):
    scaleVal = cmds.floatSliderGrp( "ant_width", q=True, v=True )
    head.widthAntenna(scaleVal)

cmds.floatSliderGrp( "ant_width", l="Antenna Width: ", v=1, cw3=[100,30,100], min=loc.ant_width[0], max=loc.ant_width[1], fmx=loc.ant_width[1], f=True, dc=widthAnt)
features.append(("ant_width", loc.ant_width, widthAnt))

cmds.separator( h=height,st="none" )

### Mandibles ###
#Width
def widthMan(*args):
    scaleVal = cmds.floatSliderGrp( "man_width", q=True, v=True )
    head.widthMandibles(scaleVal)

cmds.floatSliderGrp( "man_width", l="Mandible Width: ", v=1, cw3=[100,30,100], min=loc.man_width[0], max=loc.man_width[1], fmx=loc.man_width[1], f=True, dc=widthMan)
features.append(("man_width", loc.man_width, widthMan))

#Length
def lenMan(*args):
    scaleVal = cmds.floatSliderGrp( "man_len", q=True, v=True )
    head.lenMandibles(scaleVal)

cmds.floatSliderGrp( "man_len", l="Mandible Length: ", v=1, cw3=[100,30,100], min=loc.man_len[0], max=loc.man_len[1], fmx=loc.man_len[1], f=True, dc=lenMan)
features.append(("man_len", loc.man_len, lenMan))

#Height
def heightMan(*args):
    scaleVal = cmds.floatSliderGrp( "man_height", q=True, v=True )
    head.heightMandibles(scaleVal)

cmds.floatSliderGrp( "man_height", l="Mandible Height: ", v=1, cw3=[100,30,100], min=loc.man_height[0], max=loc.man_height[1], fmx=loc.man_height[1], f=True, dc=heightMan)
features.append(("man_height", loc.man_height, heightMan))

cmds.separator( h=height,st="none" )

### Eyes ###
#Distance
def distEyes(*args):
    scaleVal = cmds.floatSliderGrp( "eye_dist", q=True, v=True )
    head.distEyes(scaleVal)

cmds.floatSliderGrp( "eye_dist", l="Eye Distance: ", v=1, cw3=[100,30,100], min=loc.eye_dist[0], max=loc.eye_dist[1], fmx=loc.eye_dist[1], f=True, dc=distEyes)
features.append(("eye_dist", loc.eye_dist, distEyes))

#Size
def sizeEyes(*args):
    scaleVal = cmds.floatSliderGrp( "eye_size", q=True, v=True )
    head.sizeEyes(scaleVal)

cmds.floatSliderGrp( "eye_size", l="Eye Size: ", v=1, cw3=[100,30,100], min=loc.eye_scale[0], max=loc.eye_scale[1], fmx=loc.eye_scale[1], f=True, dc=sizeEyes)
features.append(("eye_size", loc.eye_scale, sizeEyes))

cmds.separator( h=height,st="none" )

### Face ###
#Length
def lenFace(*args):
    scaleVal = cmds.floatSliderGrp( "face_len", q=True, v=True )
    head.lenFace(scaleVal)

cmds.floatSliderGrp( "face_len", l="Face Length: ", v=1, cw3=[100,30,100], min=loc.face_len[0], max=loc.face_len[1], fmx=loc.face_len[1], f=True, dc=lenFace)
features.append(("face_len", loc.face_len, lenFace))

#Radius
def radFace(*args):
    scaleVal = cmds.floatSliderGrp( "face_rad", q=True, v=True )
    head.radFace(scaleVal)

cmds.floatSliderGrp( "face_rad", l="Face Radius: ", v=1, cw3=[100,30,100], min=loc.face_rad[0], max=loc.face_rad[1], fmx=loc.face_rad[1], f=True, dc=radFace)
features.append(("face_rad", loc.face_rad, radFace))

#Tilt
def tiltFace(*args):
    scaleVal = cmds.floatSliderGrp( "face_tilt", q=True, v=True )
    head.tiltFace(scaleVal)

cmds.floatSliderGrp( "face_tilt", l="Face Tilt: ", v=1, cw3=[100,30,100], min=loc.face_tilt[0], max=loc.face_tilt[1], fmx=loc.face_tilt[1], f=True, dc=tiltFace)
features.append(("face_tilt", loc.face_tilt, tiltFace))

cmds.separator( h=height,st="none" )

### Neck ###
#Scale
def scaleNeck(*args):
    scaleVal = cmds.floatSliderGrp( "neck_scale", q=True, v=True )
    head.scaleNeck(scaleVal)

cmds.floatSliderGrp( "neck_scale", l="Neck Scale: ", v=1, cw3=[100,30,100], min=loc.neck_scale[0], max=loc.neck_scale[1], fmx=loc.neck_scale[1], f=True, dc=scaleNeck)
features.append(("neck_scale", loc.neck_scale, scaleNeck))

cmds.separator( h=height,st="none" )

### THORAX ###
### Length ###
def lenThorax(*args):
    scaleVal = cmds.floatSliderGrp( "len_thx", q=True, v=True )
    thx.lenThorax(scaleVal)

cmds.floatSliderGrp( "len_thx", l="Thorax Length: ", v=1, cw3=[100,30,100], min=loc.thx_len[0], max=loc.thx_len[1], fmx=loc.thx_len[1], f=True, dc=lenThorax)
features.append(("len_thx", loc.thx_len, lenThorax))

### Scale ###
def scaleThxFront(*args):
    scaleVal = cmds.floatSliderGrp( "scale_thx_front", q=True, v=True )
    thx.scaleFront(scaleVal)

cmds.floatSliderGrp( "scale_thx_front", l="Thorax Size Front: ", v=1, cw3=[100,30,100], min=loc.thx_scale[0], max=loc.thx_scale[1], fmx=loc.thx_scale[1], f=True, dc=scaleThxFront)
features.append(("scale_thx_front", loc.thx_scale, scaleThxFront))

def scaleThxMid(*args):
    scaleVal = cmds.floatSliderGrp( "scale_thx_mid", q=True, v=True )
    thx.scaleMid(scaleVal)

cmds.floatSliderGrp( "scale_thx_mid", l="Thorax Size Mid: ", v=1, cw3=[100,30,100], min=loc.thx_scale[0], max=loc.thx_scale[1], fmx=loc.thx_scale[1], f=True, dc=scaleThxMid)
features.append(("scale_thx_mid", loc.thx_scale, scaleThxMid))

def scaleThxBack(*args):
    scaleVal = cmds.floatSliderGrp( "scale_thx_back", q=True, v=True )
    thx.scaleBack(scaleVal)

cmds.floatSliderGrp( "scale_thx_back", l="Thorax Size Back: ", v=1, cw3=[100,30,100], min=loc.thx_scale[0], max=loc.thx_scale[1], fmx=loc.thx_scale[1], f=True, dc=scaleThxBack)
features.append(("scale_thx_back", loc.thx_scale, scaleThxBack))

cmds.separator( h=height,st="none" )

### ABDOMEN ###
### Length ###
def lenAbdomen(*args):
    scaleVal = cmds.floatSliderGrp( "len_abd", q=True, v=True )
    abd.lenAbdomen(scaleVal)

cmds.floatSliderGrp( "len_abd", l="Abdomen Length: ", v=1, cw3=[100,30,100], min=loc.abd_len[0], max=loc.abd_len[1], fmx=loc.abd_len[1], f=True, dc=lenAbdomen)
features.append(("len_abd", loc.abd_len, lenAbdomen))

### Scale ###
def scaleAbdFront(*args):
    scaleVal = cmds.floatSliderGrp( "scale_abd_front", q=True, v=True )
    abd.scaleFront(scaleVal)

cmds.floatSliderGrp( "scale_abd_front", l="Abd. Size Front: ", v=1, cw3=[100,30,100], min=loc.abd_scale[0], max=loc.abd_scale[1], fmx=loc.abd_scale[1], f=True, dc=scaleAbdFront)
features.append(("scale_abd_front", loc.abd_scale, scaleAbdFront))

def scaleAbdMid(*args):
    scaleVal = cmds.floatSliderGrp( "scale_abd_mid", q=True, v=True )
    abd.scaleMid(scaleVal)

cmds.floatSliderGrp( "scale_abd_mid", l="Abd. Size Mid: ", v=1, cw3=[100,30,100], min=loc.abd_scale[0], max=loc.abd_scale[1], fmx=loc.abd_scale[1], f=True, dc=scaleAbdMid)
features.append(("scale_abd_mid", loc.abd_scale, scaleAbdMid))

def scaleAbdBack(*args):
    scaleVal = cmds.floatSliderGrp( "scale_abd_back", q=True, v=True )
    abd.scaleBack(scaleVal)

cmds.floatSliderGrp( "scale_abd_back", l="Abd. Size Back: ", v=1, cw3=[100,30,100], min=loc.abd_scale[0], max=loc.abd_scale[1], fmx=loc.abd_scale[1], f=True, dc=scaleAbdBack)
features.append(("scale_abd_back", loc.abd_scale, scaleAbdBack))

cmds.separator( h=height,st="none" )

### ARM ###
### Current Arm ###
cmds.intSliderGrp( "curr_Arm", l="Current Arm: ", v=1, cw3=[100,30,100], min=0, max=0, fmx=0, f=True)

### Tarsus ###
def lenTarsus(*args):
    scaleVal = cmds.floatSliderGrp( "arm_len_tarsus", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].lenTarsus(scaleVal)

cmds.floatSliderGrp( "arm_len_tarsus", l="Tarsus Length: ", v=1, cw3=[100,30,100], min=loc.tarsus_len[0], max=loc.tarsus_len[1], fmx=loc.tarsus_len[1], f=True, dc=lenTarsus)
features.append(("arm_len_tarsus", loc.tarsus_len, lenTarsus))

def radTarsus(*args):
    scaleVal = cmds.floatSliderGrp( "arm_rad_tarsus", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].radTarsus(scaleVal)

cmds.floatSliderGrp( "arm_rad_tarsus", l="Tarsus Radius: ", v=1, cw3=[100,30,100], min=loc.tarsus_rad[0], max=loc.tarsus_rad[1], fmx=loc.tarsus_rad[1], f=True, dc=radTarsus)
features.append(("arm_rad_tarsus", loc.tarsus_rad, radTarsus))

### Tibia ###
def lenTibia(*args):
    scaleVal = cmds.floatSliderGrp( "arm_len_tibia", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].lenTibia(scaleVal)

cmds.floatSliderGrp( "arm_len_tibia", l="Tibia Length: ", v=1, cw3=[100,30,100], min=loc.tibia_len[0], max=loc.tibia_len[1], fmx=loc.tibia_len[1], f=True, dc=lenTibia)
features.append(("arm_len_tibia", loc.tibia_len, lenTibia))

def radTibia(*args):
    scaleVal = cmds.floatSliderGrp( "arm_rad_tibia", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].radTibia(scaleVal)

cmds.floatSliderGrp( "arm_rad_tibia", l="Tibia Radius: ", v=1, cw3=[100,30,100], min=loc.tibia_rad[0], max=loc.tibia_rad[1], fmx=loc.tibia_rad[1], f=True, dc=radTibia)
features.append(("arm_rad_tibia", loc.tibia_rad, radTibia))

### Knee ###
def heightKnee(*args):
    scaleVal = cmds.floatSliderGrp( "arm_knee_height", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].heightKnee(scaleVal)

cmds.floatSliderGrp( "arm_knee_height", l="Knee Height: ", v=1, cw3=[100,30,100], min=loc.knee_height[0], max=loc.knee_height[1], fmx=loc.knee_height[1], f=True, dc=heightKnee)
features.append(("arm_knee_height", loc.knee_height, heightKnee))

### Femur ###
def lenFemur(*args):
    scaleVal = cmds.floatSliderGrp( "arm_len_femur", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].lenFemur(scaleVal)

cmds.floatSliderGrp( "arm_len_femur", l="Femur Length: ", v=1, cw3=[100,30,100], min=loc.femur_len[0], max=loc.femur_len[1], fmx=loc.femur_len[1], f=True, dc=lenFemur)
features.append(("arm_len_femur", loc.femur_len, lenFemur))

def radFemur(*args):
    scaleVal = cmds.floatSliderGrp( "arm_rad_femur", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].radFemur(scaleVal)

cmds.floatSliderGrp( "arm_rad_femur", l="Femur Radius: ", v=1, cw3=[100,30,100], min=loc.femur_rad[0], max=loc.femur_rad[1], fmx=loc.femur_rad[1], f=True, dc=radFemur)
features.append(("arm_rad_femur", loc.femur_rad, radFemur))

### Shoulder ###
def lenShoulder(*args):
    scaleVal = cmds.floatSliderGrp( "arm_len_shoulder", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].lenShoulder(scaleVal)

cmds.floatSliderGrp( "arm_len_shoulder", l="Shoudler Length: ", v=1, cw3=[100,30,100], min=loc.shoulder_len[0], max=loc.shoulder_len[1], fmx=loc.shoulder_len[1], f=True, dc=lenShoulder)
features.append(("arm_len_shoulder", loc.shoulder_len, lenShoulder))

def radShoulder(*args):
    scaleVal = cmds.floatSliderGrp( "arm_rad_shoulder", q=True, v=True )
    i = cmds.intSliderGrp( "curr_Arm", q=True, v=True ) - 1
    arms[i].radShoulder(scaleVal)

cmds.floatSliderGrp( "arm_rad_shoulder", l="Shoulder Radius: ", v=1, cw3=[100,30,100], min=loc.shoulder_rad[0], max=loc.shoulder_rad[1], fmx=loc.shoulder_rad[1], f=True, dc=radShoulder)
features.append(("arm_rad_shoulder", loc.shoulder_rad, radShoulder))

cmds.separator( h=height,st="none" )

### Spread Arms ###
def spreadArms(*args):
    scaleVal = cmds.floatSliderGrp( "spread", q=True, v=True )
    body.spreadArms(scaleVal)

cmds.floatSliderGrp( "spread", l="Arm Spread: ", v=1, cw3=[100,30,100], min=loc.spread_dist[0], max=loc.spread_dist[1], fmx=loc.spread_dist[1], f=True, dc=spreadArms)
features.append(("spread", loc.spread_dist, spreadArms))
cmds.separator( h=height,st="none" )

### WING ###
### Current Wing ###
cmds.intSliderGrp( "curr_wing", l="Current Wing: ", v=1, cw3=[100,30,100], min=0, max=0, fmx=0, f=True)

def scaleWings(*args):
    scaleVal = cmds.floatSliderGrp( "wing_scale", q=True, v=True )
    i = cmds.intSliderGrp( "curr_wing", q=True, v=True ) - 1
    wings[i].scaleWings(scaleVal)

cmds.floatSliderGrp( "wing_scale", l="Wing Scale: ", v=1, cw3=[100,30,100], min=loc.wing_scale[0], max=loc.wing_scale[1], fmx=loc.wing_scale[1], f=True, dc=scaleWings)
features.append(("wing_scale", loc.wing_scale, scaleWings))

def scaleTop(*args):
    scaleVal = cmds.floatSliderGrp( "wing_top", q=True, v=True )
    i = cmds.intSliderGrp( "curr_wing", q=True, v=True ) - 1
    wings[i].scaleTop(scaleVal)

cmds.floatSliderGrp( "wing_top", l="Wing Top: ", v=1, cw3=[100,30,100], min=loc.wing_top_scale[0], max=loc.wing_top_scale[1], fmx=loc.wing_top_scale[1], f=True, dc=scaleTop)
features.append(("wing_top", loc.wing_top_scale, scaleTop))

def scaleLow(*args):
    scaleVal = cmds.floatSliderGrp( "wing_low", q=True, v=True )
    i = cmds.intSliderGrp( "curr_wing", q=True, v=True ) - 1
    wings[i].scaleLow(scaleVal)

cmds.floatSliderGrp( "wing_low", l="Wing Low: ", v=1, cw3=[100,30,100], min=loc.wing_low_scale[0], max=loc.wing_low_scale[1], fmx=loc.wing_low_scale[1], f=True, dc=scaleLow)
features.append(("wing_low", loc.wing_low_scale, scaleLow))

# Random Generate 
def randGen(*args):

    #generateBody(True)

    #Random Features
    for feat in features:
        slider_id, ranges, command = feat
        feat_type = slider_id.split("_")[0]
        
        if feat_type == "arm":
            
            for i in range(a_arms+t_arms):
                cmds.intSliderGrp( "curr_Arm", e=True, v=i+1 )
                cmds.floatSliderGrp( slider_id, v=round(random.uniform(ranges[0], ranges[1]),2), e=True)
                command()

        elif feat_type == "wing":
            
            for i in range(w_num):
                cmds.intSliderGrp( "curr_wing", e=True, v=i+1 )
                cmds.floatSliderGrp( slider_id, v=round(random.uniform(ranges[0], ranges[1]),2), e=True)
                command()

        elif feat_type == "col":

            cmds.colorSliderGrp( slider_id, rgb=[random.uniform(ranges[0][i], ranges[1][i]) for i in range(3)], e=True)
            command()

        else: 

            cmds.floatSliderGrp( slider_id, v=round(random.uniform(ranges[0], ranges[1]),2), e=True)
            command()


cmds.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 412)],p=window)
cmds.button( label='Random', command=randGen )
cmds.separator( h=height,st="none" )

cmds.showWindow( window )

