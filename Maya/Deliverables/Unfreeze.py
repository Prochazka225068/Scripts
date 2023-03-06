import maya.cmds as cmds

selection = cmds.ls(sl=True)

for i in selection:
    
    selPos = cmds.xform(i ,q=1,ws=1,rp=1)
    
    cmds.setAttr(i + '.translate', -selPos [0], -selPos [1], -selPos [2])

    cmds.makeIdentity(i, apply=True, t=1)
    cmds.setAttr(i + '.translate', selPos [0], selPos [1], selPos [2])