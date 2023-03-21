import maya.cmds as cmds

selection = cmds.ls(sl=1)

b = cmds.duplicate(selection[0], rc=1)

children = cmds.listRelatives(allDescendents=True, type='transform')

cmds.select([b][0] + [children] )
for i in children:

    cmds.rename(i[:-1] + "_Ctrl")


selection1 = cmds.ls(sl=1)

print(selection1)
for i in selection1:
    a = cmds.duplicate(i, po=1, n=i[:-4] + "grp")
    cmds.parent(i,a)
    #cmds.pointConstraint(a, children[i])

cmds.select(selection)
c = cmds.duplicate(selection, po=1, n=selection + "_grp")

cmds.parent(b,c)

    
