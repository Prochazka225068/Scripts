import maya.cmds as cmds

selection=cmds.ls(sl=1)

curve = selection[0]
target = selection[1]

curveP = cmds.listRelatives(curve, parent=1)[0]

cmds.parent(selection, absolute=1, shape=1)

p= cmds.listRelatives(parent=1)[0]

cmds.refresh()

cmds.makeIdentity(p, apply=True, t=1, r=1, s=1, n=0, pn=1)

def step_two():
    cmds.parent(curve, target, relative=True, shape=True)
    cmds.delete(curveP)

    children = cmds.listRelatives(curveP, children=True)
    if children == None:
        cmds.delete(curveP)

    cmds.rename(curve, target+"Shape", ignoreShape=False)

cmds.evalDeferred("step_two()")