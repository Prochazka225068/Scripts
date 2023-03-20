import maya.cmds as cmds

selPaths = cmds.ls(sl=True)

for i in selPaths:

    cmds.connectAttr('Main_Root.L_Tracks', i + '.input', f = 1)