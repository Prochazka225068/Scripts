import maya.cmds as cmds

selection = cmds.ls(sl=1)

curves = selection[0]
target = selection[1]

curvesP = cmds.listRelatives(curves, parent=1)[0]
cmds.parent(selection, absolute=1, shape=1)
p = cmds.listRelatives(parent=1)[0]
cmds.refresh()
cmds.makeIdentity(p, apply=1, t=1, r=1, n=0, pn=1)

def step_two():
    cmds.parent(curves, target, absolute=1, shape=1)
    cmds.delete(p)

    children = cmds.listRelatives(curvesP, children=1)
    if children == None:
        cmds.delete(curvesP)

    cmds.rename(curves, target+'Shape', ignoreShape=0)

cmds.evalDeferred('step_two()')