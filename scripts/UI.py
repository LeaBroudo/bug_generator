import maya.cmds as cmds
import pydoc
import random
import main 
import head_control
import regions as loc
from functools import partial


#def createUI():

body = main.Body()
head = head_control.Head()
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
    body.importAll(name, w_num, a_arms, t_arms)
# global head
    #head = head_control.Head(name)

    
cmds.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 412)],p=window)
cmds.button( label='Generate Body', command=generateBody )

#FOR LOOP FOR ALL BUTTONS



### HEAD ###
### Antenna ###
#length
def lenAnt(*args):
    scaleVal = cmds.intSliderGrp( "ant_len", q=True, v=True )
    head.lengthAntenna(scaleVal)

cmds.intSliderGrp( "ant_len", l="Antenna Len: ", v=1, cw3=[100,30,100], min=loc.ant_len[0], max=loc.ant_len[1], fmx=loc.ant_len[1], f=True, dc=lenAnt)

#width
def widthAnt(*args):
    scaleVal = cmds.intSliderGrp( "ant_width", q=True, v=True )
    head.widthAntenna(scaleVal)

cmds.intSliderGrp( "ant_width", l="Antenna Width: ", v=1, cw3=[100,30,100], min=loc.ant_width[0], max=loc.ant_width[1], fmx=loc.ant_width[1], f=True, dc=widthAnt)

### Mandibles ###
#Width
def widthMan(*args):
    scaleVal = cmds.intSliderGrp( "man_width", q=True, v=True )
    head.widthMandibles(scaleVal)

cmds.intSliderGrp( "man_width", l="Mandible Width: ", v=1, cw3=[100,30,100], min=loc.man_width[0], max=loc.man_width[1], fmx=loc.man_width[1], f=True, dc=widthMan)

#Length
def lenMan(*args):
    scaleVal = cmds.intSliderGrp( "man_len", q=True, v=True )
    head.lenMandibles(scaleVal)

cmds.intSliderGrp( "man_len", l="Mandible Length: ", v=1, cw3=[100,30,100], min=loc.man_len[0], max=loc.man_len[1], fmx=loc.man_len[1], f=True, dc=lenMan)

#Height
def heightMan(*args):
    scaleVal = cmds.intSliderGrp( "man_height", q=True, v=True )
    head.heightMandibles(scaleVal)

cmds.intSliderGrp( "man_height", l="Mandible Height: ", v=1, cw3=[100,30,100], min=loc.man_height[0], max=loc.man_height[1], fmx=loc.man_height[1], f=True, dc=heightMan)



cmds.showWindow( window )