import maya.cmds as cmds

#Generates a cube with custom name and size
def cubeMaker(name,size):
    
    a = cmds.curve(n=name, d=1,p=[(-size/2,-size/2,-size/2),(size/2,-size/2,-size/2),(size/2,-size/2,size/2),(-size/2,-size/2,size/2),(-size/2,-size/2,-size/2),
                                   (-size/2,size/2,-size/2),(size/2,size/2,-size/2),(size/2,-size/2,-size/2),(size/2,size/2,-size/2),
                                   (size/2,size/2,size/2),(size/2,-size/2,size/2),(size/2,size/2,size/2),
                                   (-size/2,size/2,size/2),(-size/2,-size/2,size/2),(-size/2,size/2,size/2),(-size/2,size/2,-size/2)])


def alignObj():
    #takes selected objects aligns rot and pos to first selected
    selObj= cmds.ls(sl=True)

    position= cmds.xform(selObj[0], q=True, ws=True, t=True)
    rotation= cmds.xform(selObj[0], q=True, ws=True, ro=True)

    for i in selObj:
        cmds.xform(i, ws=True, t=[position[0], position[1], position[2]])
        cmds.xform(i, ws=True, ro=[rotation[0], rotation[1],rotation[2]])

#User Interface
window= cmds.window(t="Jan Prochazka wire cube creator", w=400, h=250)
cmds.columnLayout()
cmds.text(l='Cube Name')
cubename=cmds.textFieldGrp(tx="")

cmds.text(l='Size')
cubesize=cmds.textFieldGrp(tx="")

cmds.button(l="create controller", w=250, h=25, c="cubeMaker(cmds.textFieldGrp(cubename,q=True, tx=True),float(cmds.textFieldGrp(cubesize, q=True, tx=True)))")
cmds.button(l="snap to object", w=250, h=25, c="alignObj()")
cmds.showWindow()