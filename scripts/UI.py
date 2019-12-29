import maya.cmds as cmds
import pydoc
import random
import main 


body = None
name = ""
w_num = 0
a_arms = 0
t_arms = 0

def createUI():
    
    window = cmds.window( title="Bug Generator", iconName="Bug Generator", widthHeight=(412, 600) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.text(label="Bug Generator", font="boldLabelFont")
    cmds.separator( height=10 )

    # Name
    cmds.rowColumnLayout( nc=2, cw=[(1,40),(2,100)], p=window )
    cmds.text("Name: ", en=True)
    cmds.textField( "bug_name", en=True, tx="Bug") #must connect this to some variable

    # Arms/Wings
    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 270),(2, 50)],p=window)
    
    cmds.intSliderGrp( "thoraxArms", l="Thorax Arms: ", v=2, cw3=[40,30,200], min=0, max=3, fmx=3, f=True) 
    thorax_rand = cmds.checkBox( "thorax_rand", value=False )
    cmds.intSliderGrp( "abdomenArms", l="Abdomen Arms: ", v=2, cw3=[40,30,200], min=0, max=3, fmx=3, f=True) 
    abdomen_rand = cmds.checkBox( "abdomen_rand", value=False )
    
    cmds.intSliderGrp( "wings", l="Wings: ", v=2, cw3=[40,30,200], min=0, max=2, fmx=2, f=True) 
    wing_rand = cmds.checkBox( "wing_rand", value=False )

    # Form body 
    def generateBody(*args):
        
        #Name
        global name
        name = str(cmds.textField( "bug_name", q=True, tx=True ))
        
        global w_num, a_arms, t_arms
        #Thorax Arm num
        if cmds.checkBox( "thorax_rand", q=True, v=True ) == True:
            t_arms = random.randint(0,5)
        else:
            t_arms = cmds.intSliderGrp( "thoraxArms", q=True, v=True )

        #Abdomen Arm num
        if cmds.checkBox( "abdomen_rand", q=True, v=True ) == True:
            a_arms = random.randint(0,5)
        else:
            a_arms = cmds.intSliderGrp( "abdomenArms", q=True, v=True )
        
        #Wing num
        if cmds.checkBox( "wing_rand", q=True, v=True ) == True:
            w_num = random.randint(0,5)
        else:
            w_num = cmds.intSliderGrp( "wings", q=True, v=True )
        
        #Create body
        global body
        body = main.Body(name, w_num, a_arms, t_arms)
        
    cmds.button( label='Generate Body', command=generateBody )

    #Select Arm to edit 
    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 270),(2, 50)],p=window)
    cmds.intSliderGrp( "curr_thorax_arm", l="Thorax Arm: ", v=0 if t_arms==0 else 1, cw3=[40,30,200], min=0, max=t_arms, fmx=t_arms, f=True) 
    cmds.intSliderGrp( "curr_abdomen_arm", l="Abdomen Arm: ", v=0 if a_arms==0 else 1, cw3=[40,30,200], min=0, max=a_arms, fmx=a_arms, f=True) 







    #Select Wing to edit 
    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 270), (2, 50)],p=window)
    cmds.intSliderGrp( "curr_thorax_arm", l="Thorax Arm: ", v=0 if w_num==0 else 1, cw3=[40,30,200], min=0, max=w_num, fmx=w_num, f=True) 

    cmds.showWindow( window )