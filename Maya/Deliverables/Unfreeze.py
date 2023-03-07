import maya.cmds as cmds

selection = cmds.ls(sl=True)

for i in selection:
    
    selPos1 = cmds.xform(i ,q=1,ws=1,rp=1)
    cmds.setAttr(i + '.translate', 0, 0, 0)
    selPos0 = cmds.xform(i ,q=1,ws=1,rp=1)
    cmds.setAttr(i + '.translate', -selPos0 [0], -selPos0 [1], -selPos0 [2])
    cmds.makeIdentity(i, apply=True, t=1)
    cmds.setAttr(i + '.translate', selPos1 [0], selPos1 [1], selPos1 [2])