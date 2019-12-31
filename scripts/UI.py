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
        body = main.Body(name, w_num, a_arms, t_arms)
        
    cmds.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 412)],p=window)
    cmds.button( label='Generate Body', command=generateBody )

    #FOR LOOP FOR ALL BUTTONS
    

    cmds.showWindow( window )