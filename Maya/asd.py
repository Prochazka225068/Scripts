import maya.cmds as cmds
selpaths = cmds.ls(sl=True)

for all in selpaths:

    cmds.connectAttr('Root_ctrl.l_trackguide',all +'.input',f = True)
    cmds.air